FROM python:3.10-slim

WORKDIR /app

RUN mkdir .aws
COPY credentials ./.aws

COPY ./requirements.txt .
RUN apt-get update && apt-get install git -y
RUN pip3 install -r requirements.txt
RUN pip3 install "git+https://github.com/openai/whisper.git" 
RUN apt-get install -y ffmpeg

COPY ./transcribe.py .

ENTRYPOINT ["python3", "transcribe.py", "tests.videos.untranscribed", "tests.text.transcribed", "video.mp4"]
