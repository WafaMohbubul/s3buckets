#DELETE BUCKET
import boto3

s3 = boto3.client('s3')

bucket_name = "tech254-wafa-bucket"

s3.delete_bucket(Bucket=bucket_name)


#DELETE FILE
import boto3

s3 = boto3.client('s3')

response = s3.delete_object(Bucket="tech254-wafa-bucket", Key="example.txt")

print(response)
