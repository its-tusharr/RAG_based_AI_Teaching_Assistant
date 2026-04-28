 RAG_based_AI_Teaching_Assistant - An intelligent teaching assistant powered by Retrieval-Augmented Generation (RAG) that combines large language models with contextual knowledge retrieval to deliver accurate, personalized, and explainable learning support.

This project leverages modern NLP techniques to answer questions, generate explanations, and assist learners by grounding responses in relevant documents, ensuring both reliability and depth in educational interactions.
# How to use this RAG AI Teaching Assistant on your own data
## Step 1 - Collect your videos
Move all your video files to the video folder

## Step 2 - Convert into mp3
Convert all the video files to mp3 by running video_to_mp3

## Step 3 - Convert mp3 to json
Convert all the mp3 files to json by running mp3_to_json

## Step 4 - COnvert the jsons files to Vectors
Use the file preproces_json to convert the json files to a dataframe with embedding and save it as a joblib pickle 

## Step 5 - Prompt Generation and Feeding to the LLM
Read the joblib file and load it into the memory. Then create a relevent prompt as per the user query to feed it to the LLM.
