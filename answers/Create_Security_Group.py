# This is the answer of Original Tutorial: Create Security Group

from aws_cdk.core import App, Construct
from aws_cdk import (
    aws_ec2 as ec2,
    core
    )
import boto3


class sgStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        ec2 = boto3.client('ec2')
        response = ec2.describe_vpcs()
        vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
                
    #Set SG name and description
        response = ec2.create_security_group(GroupName='MySecurityGroup',
                                             Description='Allow access to MyInstance',
                                             VpcId=vpc_id)
        security_group_id = response['GroupId']
    
    #Set Inbound rules
        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])