

import boto3
import json

def lambda_handler(event, context):
    # Specify the S3 bucket name for which you want to enable block public access
    bucket_name = event['detail']['requestParameters']['bucketName']
    
    public_accessconfig= event['detail']['requestParameters']['PublicAccessBlockConfiguration']
    
    if public_accessconfig['RestrictPublicBuckets'] == False and public_accessconfig['BlockPublicPolicy'] == False and public_accessconfig['BlockPublicAcls'] == False and public_accessconfig['IgnorePublicAcls'] == False:
        #print('PublicAccessBlockConfiguration')


        # Create an S3 client
        s3_client = boto3.client('s3')
    
        # Enable block public access for the bucket
        try:
            s3_client.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )
            print(f"Block public access enabled for S3 bucket: {bucket_name}")
        except Exception as e:
            print(f"Error enabling block public access for S3 bucket {bucket_name}: {str(e)}")
            
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda is Executed!')
    }        
    
        # Optionally, you can return a response or take additional actions here




#S3blockpublicaccessACL

import boto3
import json

def lambda_handler(event, context):
    # Specify the S3 bucket name for which you want to enable block public access
    bucket_name = event['requestParameters']['bucketName']
    
    public_accessconfig= event['requestParameters']['PublicAccessBlockConfiguration']
    
    if public_accessconfig['RestrictPublicBuckets'] == False and public_accessconfig['BlockPublicPolicy'] == False and public_accessconfig['BlockPublicAcls'] == False and public_accessconfig['IgnorePublicAcls'] == False:
        #print('PublicAccessBlockConfiguration')


        # Create an S3 client
        s3_client = boto3.client('s3')
    
        # Enable block public access for the bucket
        try:
            s3_client.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )
            print(f"Block public access enabled for S3 bucket: {bucket_name}")
        except Exception as e:
            print(f"Error enabling block public access for S3 bucket {bucket_name}: {str(e)}")
            
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda is Executed!')
    }        
    