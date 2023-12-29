import boto3

def lambda_handler(event, context):
    
    ec2_client = boto3.client('ec2')
    InstanceID = event['detail']['requestParameters']['instanceId']
    AllocID = event['detail']['requestParameters']['allocationId']
    AssocID = event['detail']['responseElements']['associationId']
    
    
            
    try:
        # Disassociate the Elastic IP from the EC2 instance
        ec2_client.disassociate_address(AssociationId=AssocID)
                
                # Release the Elastic IP to prevent charges
        ec2_client.release_address(AllocationId=AllocID)
        print(f"Remediated Elastic IP from EC2 instance {InstanceID}")
            
    except Exception as e:
        print(f"Failed to remediate Elastic IP on EC2 instance {InstanceID}: ")
    
    return {
        'statusCode': 200,
        'body': 'Elastic IPs remediated successfully'
    }
