import boto3

s3_client = boto3.client('s3')

bucket_content = s3.upload_file("testfile.txt", bucket_name, "testfile2.txt")

print(bucket_content)`