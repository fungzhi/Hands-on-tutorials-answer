# This is the answer of Original Tutorial: Create A Security Group

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt
    
    # cdk ls   (output: CreateSecurityGroup)
    
    # delete line 36 and line 56 ["""]

    # cdk deploy CreateSecurityGroup (go check the CoudFormation and there will be a stack called "CreateSecurityGroup", check security group will see the newly created sg)
    
    # Answer deployed!

    # To prevent effects other answers, please remember to delete the new security group, "CreateSecurityGroup" stack and add ["""] again in lines 36, 56 again after checking the answer


from aws_cdk import core
import aws_cdk.aws_ec2 as ec2
import boto3


ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')


class sgStack(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
        
"""  
    #Create a security group with default vpc(Set SG name and description)
        response = ec2.create_security_group(GroupName='EC2 Security Group',
                                             Description='Allow access to MyInstance',
                                             VpcId=vpc_id)
        security_group_id = response['GroupId']
    
    #Set Inbound rules(example rules for allow access to instance)
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
"""