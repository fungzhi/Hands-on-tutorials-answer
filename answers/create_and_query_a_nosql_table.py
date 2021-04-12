# Hands-on Lab: Create and Query a NoSQL Table
# Tutorial Link: https://aws.amazon.com/getting-started/hands-on/create-nosql-table/

# This is the answer of Hands-on Tutorial: Create and Query a NoSQL Table

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt ( aws-cdk.aws-dynamodb )
    
    # cdk ls   (Output: DynamodbNoSqlTable)
    
    # cdk deploy DynamodbNoSqlTable
        # (Go check the CloudFormation and there will be a stack called "DynamodbNoSqlTable")
    
# Answer deployed!

from aws_cdk import (
    core,
    aws_dynamodb as dynamodb
)


class CreateDynamodbNoSqlTable(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an Amazon DynamoDB a NoSQL Table: "Music"
        table = dynamodb.Table(
            self, "Music",
            partition_key = dynamodb.Attribute(name = "Artist", type = dynamodb.AttributeType.STRING),
            sort_key = dynamodb.Attribute(name = "SongTitle", type = dynamodb.AttributeType.STRING),
            removal_policy = core.RemovalPolicy.DESTROY
        )
        # Try the below steps like the tutorial then you will succeed:
            # Add data to the NoSQL Table
            # Querry the NoSQL Table
        
#  You may delete your stack(DynamodbNoSqlTable) to clean up your environment

    # cdk destroy DynamodbNoSqlTable
        # (Go check the CloudFormation a stack called "DynamodbNoSqlTable" will be destroyed)

# Clean up finished!