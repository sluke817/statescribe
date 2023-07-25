import whisper
import boto3
import sys

# s3 = boto3.resource("s3")
# for bucket in s3.buckets.all():
#     print(bucket.name)

print("Loading model...")
model = whisper.load_model("large")
print("Complete!")

bucket_from = sys.argv[1]
bucket_to = sys.argv[2]
file_to_transcribe = sys.argv[3]

print("Loading video...")
client = boto3.client("s3")
client.download_file(
    Bucket=bucket_from, Key=file_to_transcribe, Filename="video"
)
print("Complete!")

print("Transcribing video...")
result = model.transcribe("./video")

txt_file = open("text.txt", "w")

txt_file.write(result["text"])
print("Complete!")

print("Uploading text...")
client.upload_file(
    Filename="text.txt",
    Bucket=bucket_to,
    Key=file_to_transcribe + ".transcription"
)
