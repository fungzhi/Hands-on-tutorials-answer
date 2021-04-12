# This is the answer of Tutorial: Introduction to Amazon DynamoDB Activity Guide

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt ( aws-cdk.aws-dynamodb )
    
    # cdk ls   (output: IntroductionToAmazonDynamoDBActivityGuide)
    
    # cdk deploy IntroductionToAmazonDynamoDBActivityGuide   (go check the CoudFormation and there will be a stack called "IntroductionToAmazonDynamoDBActivityGuide")

    # Answer deployed!
    
    
from aws_cdk.core import App, Construct
from aws_cdk import (
    aws_dynamodb as dynamodb,
    core
    )
from aws_cdk.aws_dynamodb import Attribute, AttributeType, Table


class CreateDynamoDBTable(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        
        table = Table(
            # Create a DynamoDB table //
            self, "ANS-Music", 
            # Create Partition key and sort key //
            partition_key=Attribute(name="Artist", type=AttributeType.STRING),
            sort_key=Attribute(name="Song", type=AttributeType.STRING),
            )
        
        
        