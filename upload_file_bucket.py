import boto3

s3_client = boto3.client('s3')

bucket_content = s3.upload_file("testfile.txt", bucket_name, "example.txt")

print(bucket_content)`