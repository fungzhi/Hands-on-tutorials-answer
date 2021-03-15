# This is the answer of Tutorial: Launching and configuring an Amazon EC2 instance Activity Guide

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt ( aws-cdk.aws-ec2 )
    
    # cdk ls   (output: LaunchingAndConfiguringAnAmazonEC2InstanceActivityGuide)
    
    # cdk deploy LaunchingAndConfiguringAnAmazonEC2InstanceActivityGuide   (go check the CoudFormation and there will be a stack called "LaunchingAndConfiguringAnAmazonEC2InstanceActivityGuide")

    # Answer deployed!
    
    
from aws_cdk.core import App, Construct
from aws_cdk import (
    aws_ec2 as ec2,
    core
    )


class CreateVPC(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        
        MyVPC = ec2.Vpc(
            # VPC name //
            self, "ANS-VPC", 
            # Public subnet's IPv4 CIDR //
            cidr="10.0.0.0/16", 
            # Configures the maximum number of availability zones as 1 //
            max_azs=1,
            # No nat gateway //
            nat_gateways=0,
            subnet_configuration=[
                # Create a public subnet with 24 CIDR mask //
                ec2.SubnetConfiguration(
                    name="Public",
                    cidr_mask=24,
                    subnet_type=ec2.SubnetType.PUBLIC),
                # Isolated subnets ( will not route to nat gateway ) //
                ec2.SubnetConfiguration(
                    name="Private",
                    cidr_mask=24,
                    subnet_type=ec2.SubnetType.ISOLATED)
                ]
            )
            
            
        # Add tag to all items //
        core.Tag.add(MyVPC, key="Owner", value="MyVPC")
        
        # One VPC was created (with cidr: 10.0.0.0/16)
        # Please check your items in ANS-VPC: one internet gateway, one AZs, one public subnet and private subnet(isolated subnet)
        # PublicSubnets route to the internet gateway