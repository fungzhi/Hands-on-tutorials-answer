# Hands-on Lab: Send Messages Between Distributed Applications
# Tutorial Link: https://aws.amazon.com/getting-started/hands-on/send-messages-distributed-applications

# This is the answer of Hands-on Tutorial: Send Messages Between Distributed Applications

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt ( aws-cdk.aws-sqs )
    
    # cdk ls   (Output: SendMessagesQueue)
    
    # cdk deploy SendMessagesQueue
        # (Go check the CloudFormation and there will be a stack called "SendMessagesQueue")
    
# Answer deployed!

from aws_cdk import (
    core,
    aws_sqs as sqs
)

class CreateSqsQueue(core.Stack):
    
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
    
        # Create an Amazon SQS Queue: "Orders"
        queue = sqs.Queue(self, "Orders", queue_name="Orders")

        # Try to Send Messages to the Queue like the tutorial(Step 3) then you will succeed
        
#  You may delete your stack(SendMessagesQueue) to clean up your environment

    # cdk destroy SendMessagesQueue
        # (Go check the CloudFormation a stack called "SendMessagesQueue" will be destroyed)

# Clean up finished!