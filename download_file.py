import boto3

s3_client = boto3.client('s3')

s3_client.download_file(input("Enter bucket name: "), input("Enter object name: "), input("Enter file name: "))