import boto3

s3 = boto3.client('s3')

response = s3.delete_object(Bucket="tech254-wafa-bucket", Key="example.txt")

print(response)