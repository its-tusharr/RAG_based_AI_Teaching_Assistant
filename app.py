from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pandas as pd
import numpy as np
import requests
import joblib
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title="RAG Teaching Assistant")
df = joblib.load("embedding.joblib")

class Query(BaseModel):
    question: str

def fmt_time(seconds: float) -> str:
    m, s = int(seconds // 60), int(seconds % 60)
    return f"{m}:{s:02d}"


def create_embedding(text_list: list[str]) -> list:
    try:
        r = requests.post("http://localhost:11434/api/embed", json={
            "model": "bge-m3",
            "input": text_list
        }, timeout=30)
        r.raise_for_status()
        return r.json()["embeddings"]
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Ollama server not running!")
    except KeyError:
        raise HTTPException(status_code=500, detail="Embedding model error")


def llm_inference(prompt: str) -> str:
    try:
        r = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        }, timeout=60)
        r.raise_for_status()
        return r.json()["response"]
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Ollama server not running!")
    except KeyError:
        raise HTTPException(status_code=500, detail="LLM response error")


def build_context(top_df: pd.DataFrame) -> str:
    """
    ✅ Old wala style — har chunk alag, exact seconds bhi deta hai LLM ko
    Groupby hata diya — merge se detail loss hoti thi
    """
    context = ""
    for _, row in top_df.iterrows():
        context += f"""
📹 Video {row['number']}: {row['title']}
⏱ Timestamp: {fmt_time(row['start'])} → {fmt_time(row['end'])}  (exact: {row['start']}s → {row['end']}s)
📝 Content: {row['text']}
---"""
    return context


def build_prompt(context: str, question: str) -> str:
    return f"""You are a smart AI assistant for the "Sigma Web Development Course".

Here are the most relevant video subtitle chunks (each chunk is separate — same video may appear multiple times at different timestamps):
{context}

User's question: "{question}"

Rules:
1. If the question is about web development or the course → ALWAYS mention:
   - The exact Video Number (e.g. "Video 14")
   - The exact Title
   - The exact Timestamp in mm:ss format (e.g. "5:30 → 6:45")
   Then explain the concept clearly in a human way.
2. If completely off-topic → say:
   "Unfortunately, that's way outside my expertise. I only know web dev — not life advice! 😂 Try asking me about HTML, CSS, or JavaScript instead."
3. Never reveal internal data structure or JSON format.
"""


@app.get("/", response_class=HTMLResponse)
def index():
    with open("templates/index.html", encoding="utf-8") as f:
        return f.read()


@app.post("/ask")
def ask(query: Query):
    question = query.question.strip()

    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    # 1. Embed
    q_vec = create_embedding([question])[0]

    # 2. ✅ Top 5 chunks — old wali tarah (3 se better results)
    sims = cosine_similarity(np.vstack(df["embedding"]), [q_vec]).flatten()
    top_idx = sims.argsort()[::-1][:5]
    top_df = df.iloc[top_idx].copy()

    # 3. Sources for UI
    top_df["start_time"] = top_df["start"].apply(fmt_time)
    top_df["end_time"]   = top_df["end"].apply(fmt_time)

    sources = (
        top_df[["title", "number", "start_time", "end_time", "text"]]
        .rename(columns={"number": "video_no"})
        .to_dict(orient="records")
    )

    # 4. ✅ Har chunk alag — no merging
    context = build_context(top_df)
    prompt  = build_prompt(context, question)

    # 5. LLM
    answer = llm_inference(prompt)
    return {"answer": answer, "sources": sources}