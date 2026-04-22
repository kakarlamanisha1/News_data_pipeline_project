import boto3

# AWS Credentials
AWS_ACCESS_KEY = "YOUR_KEY"
AWS_SECRET_KEY = "YOUR_KEY"

BUCKET_NAME = "news-data-raw-bucket-manisha"
LOCAL_FILE = "/opt/airflow/scripts/news.csv"
S3_FILE = "processed/news.csv"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_FILE)

print("news.csv uploaded to S3 successfully")