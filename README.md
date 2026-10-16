# 🎓 RAG-Based AI Teaching Assistant

An AI-powered teaching assistant that enables students to ask questions about video lectures and receive context-aware answers based on lecture content. The project combines speech-to-text transcription, text embeddings, semantic search, and Retrieval-Augmented Generation (RAG) to make educational videos searchable and interactive.

## 🚀 Project Overview

Traditional video lectures require students to search manually through long recordings to find specific information. This project aims to simplify learning by transforming lecture content into a searchable knowledge base.

The system processes lecture videos, extracts their audio, converts speech into text, retrieves relevant lecture content for a user's question, and uses a Large Language Model (LLM) to generate a contextual response.

## ✨ Key Features

- **Video-to-Text Conversion:** Extracts audio from lecture videos and transcribes spoken content.
- **Semantic Search:** Finds relevant lecture passages based on the meaning of a question rather than exact keyword matches.
- **Retrieval-Augmented Generation (RAG):** Grounds generated answers in retrieved lecture content.
- **Local LLM Support:** Uses Ollama to run a compatible language model locally, reducing dependence on hosted LLM APIs.
- **Context-Aware Question Answering:** Enables students to ask questions about lecture topics and receive relevant explanations.
- **Modular Pipeline:** Separates audio processing, transcription, retrieval, and answer generation into distinct stages.

## 🛠️ Technology Stack and Its Role

| Technology | Purpose |
|---|---|
| Python | Core programming language used to build the processing and retrieval pipeline |
| OpenAI Whisper | Converts spoken lecture audio into text |
| FFmpeg | Extracts audio from video files and supports audio preprocessing |
| Ollama | Runs a supported LLM locally for answer generation |
| Text Embedding Model | Converts text chunks and user questions into numerical vector representations |
| Vector Database / Vector Index | Stores and searches embeddings to retrieve relevant lecture content |
| RAG Pipeline | Connects retrieval results with the LLM to produce context-aware answers |
| Jupyter Notebook | Supports experimentation, development, and testing of the pipeline |

*Note: The embedding model and vector storage technology should be replaced with the exact implementations used in the project.*

## 🏗️ System Architecture

The project follows a Retrieval-Augmented Generation workflow:

**Lecture Video → Audio Extraction → Speech Transcription → Text Chunking → Embeddings → Vector Storage → Semantic Retrieval → Ollama LLM → Answer**

### How Each Stage Works

**1. Video and Audio Processing**
- Input lecture videos are processed using FFmpeg.
- Audio is extracted into a format suitable for transcription.

**2. Speech-to-Text Transcription**
- OpenAI Whisper converts lecture audio into text.
- The resulting transcript provides the textual content used by the retrieval pipeline.

**3. Text Chunking**
- The transcript is divided into smaller, manageable sections.
- Chunking helps retrieve relevant passages instead of processing the entire lecture for every question.

**4. Embedding Generation**
- An embedding model converts each text chunk into a numerical vector.
- These vectors represent semantic information about the lecture content.

**5. Vector Storage and Semantic Search**
- The embeddings and their associated text chunks are stored in a searchable vector index or database.
- A student's question is embedded and compared with stored lecture vectors to identify relevant passages.

**6. Retrieval-Augmented Generation**
- The most relevant passages are provided as context to the language model.
- The model uses the retrieved content to generate a response related to the lecture.

**7. Local LLM Inference with Ollama**
- Ollama manages the execution of a compatible locally hosted language model.
- The model receives the user's question and retrieved context to generate the final answer.

## 📂 Project Workflow

1. Provide a lecture video as input.
2. Extract its audio using FFmpeg.
3. Transcribe the audio using Whisper.
4. Split the transcript into smaller text chunks.
5. Generate embeddings and index the chunks.
6. Accept a question from the student.
7. Retrieve semantically relevant lecture passages.
8. Pass the question and retrieved context to the Ollama-hosted LLM.
9. Return a context-aware answer to the student.

## 💻 Installation and Setup

### Prerequisites

- Python installed on your system
- FFmpeg installed and accessible from the command line
- Ollama installed if using local LLM inference
- A compatible language model downloaded through Ollama
- The embedding model and vector storage dependencies used by your implementation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

If you maintain a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies specified by your actual implementation.

### 4. Configure Ollama

Install Ollama and download a compatible model:

```bash
ollama pull <YOUR_MODEL_NAME>
```

Start the Ollama service if it is not already running, and ensure the selected model is available locally.

### 5. Run the Project

Run the notebook or application entry point provided in the repository. Follow the project-specific instructions for supplying lecture videos, creating the knowledge base, and asking questions.

*The setup commands above are templates; replace placeholders and execution instructions with your actual project configuration.*

## 🎯 Use Cases

- Quickly finding explanations from lengthy lecture videos
- Revising concepts before examinations
- Asking follow-up questions about educational material
- Creating searchable knowledge bases from recorded classes
- Supporting self-paced learning and lecture revision

## ⚠️ Current Limitations

- Transcription accuracy depends on audio quality, language, and background noise.
- Large speech-recognition models can require substantial RAM and processing resources.
- Answer quality depends on the relevance of retrieved passages and the capabilities of the selected LLM.
- The system's ability to provide reliable answers depends on the coverage and quality of the indexed lecture material.

## 🔮 Future Improvements

- Add a user-friendly web interface for uploading lectures and asking questions.
- Support multiple lecture videos and searchable course collections.
- Include timestamps and source references in retrieved answers.
- Improve retrieval quality using metadata filtering and reranking.
- Optimize model selection and inference for resource-constrained systems.

## 📚 Learning Outcomes

Through this project, I explored:

- Retrieval-Augmented Generation (RAG) architecture
- Speech recognition and audio preprocessing
- Text chunking and vector embeddings
- Semantic search and information retrieval
- Local Large Language Model inference using Ollama
- Integration of multiple AI components into an end-to-end pipeline

## 👨‍💻 Author

**Tushar**

B.Tech in Computer Science & Information Technology | 2026

Interested in Data Science, Machine Learning, Generative AI, and AI-powered applications.

---

⭐ If you find this project useful, consider giving the repository a star!
