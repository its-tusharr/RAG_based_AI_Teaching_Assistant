import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib

def create_embedding(text_list):
    r=requests.post('http://localhost:11434/api/embed',json={
        "model": "bge-m3",
        "input": text_list
        }
        )
    embedding=r.json()['embeddings']
    return embedding 
def inference(prompt):
    r=requests.post('http://localhost:11434/api/generate',json={
        #"model": "deepseek-r1",
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream":False
        }
        )
    response=r.json()
    print(response)
    return response





df=joblib.load('embedding.joblib')

input_query=input("Ask a question: ")
question_query=create_embedding([input_query])[0]

#print(question_query)

#print(np.vstack(df['embedding'].values))
#print(np.vstack(df['embedding']).shape)
#find similarity of question_embedding with other embedding
similarity=cosine_similarity(np.vstack(df['embedding']),[question_query]).flatten()
top_result=5
max_indx=similarity.argsort()[::-1][0:top_result]
#print(max_indx)
new_df=df.loc[max_indx]
#print(new_df[['title','number','text']])

prompt=f'''I am teaching web development in my Sigma Web Development Course. Here are video subtitle chunks containing video title , video number , start time in seconds , end time in seconds , the text at that time : 

{new_df[['title','number','text','start','end']].to_json(orient='records')}
------------------------------------
"{input_query}"
User asked this question related to the video chunks, you have to answer in a humay way (don't mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer the questions related to the course
'''

for index,item in new_df.iterrows():
    print(index, item['title'], item['number'], item['text'], item['start'], item['end'])

with open('prompt.txt','w') as f:
    f.write(prompt)

response=inference(prompt)["response"]
print(response)

with open('response.txt','w') as f:
    f.write(response)