import boto3
import json

def remediate_security_group(event, context):
    ec2 = boto3.client('ec2')
    #print(event)
    security_group_id = event['detail']['requestParameters']['groupId']
    #print(event)
    
    # Get the existing inbound rules for the security group
    response = ec2.describe_security_groups(GroupIds=[security_group_id])
    security_group = response['SecurityGroups'][0]
    
    # Iterate through the inbound rules and revoke those with open access to 0.0.0.0/0
    revoked_rules = []
    for permission in security_group['IpPermissions']:
        for ip_range in permission.get('IpRanges', []):
            if ip_range['CidrIp'] == '0.0.0.0/0':
                revoked_rules.append(permission)
                
    print(revoked_rules)
    # Revoke the identified rules
    if revoked_rules:
        ec2.revoke_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=revoked_rules
        )
        print(f"Revoked {len(revoked_rules)} rules for {security_group_id}")
    else:
        print(f"No rules to revoke for {security_group_id}")
    #    
def lambda_handler(event, context):
    remediate_security_group(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda is Executed!')
    }        