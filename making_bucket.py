#import boto3
import boto3

bucket_name = "tech254-wafa-bucket"
def create_bucket(bucket_name):
    region = "eu-west-1"
    s3_client = boto3.client('s3', region)
    location = {'LocationConstraint': region}
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

name = "tech254-wafa-bucket"
create_bucket(name)

