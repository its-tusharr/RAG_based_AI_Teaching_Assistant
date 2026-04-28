import os
import subprocess

files=os.listdir("videos")
for file in files:
    tutorial_number=file.split('(')[0].split('#')[1]
    file_name=file.split('___S')[0]
    print(file_name,tutorial_number)
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audio/{tutorial_number}_{file_name}.mp3"]) 