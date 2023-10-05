import boto3

s3_client = boto3.client('s3')

s3_client.download_file(Bucket="tech254-wafa-bucket", Key="example.txt", "testfile.txt")