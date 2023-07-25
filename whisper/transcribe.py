import whisper
import boto3
import sys

model = whisper.load_model("large")

bucket_from = sys.argv[1]
bucket_to = sys.argv[2]
file_to_transcribe = sys.argv[3]

client = boto3.client("s3")
client.download_file(
    Bucket=bucket_from, Key=file_to_transcribe, Filename="video"
)

result = model.transcribe("./video")

txt_file = open("text.txt", "w")

txt_file.write(result["text"])

client.upload_file(
    Filename="text.txt",
    Bucket=bucket_to,
    Key=file + ".transcription"
)
