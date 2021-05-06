# A Cloud Guru Hand on lab: Creating a Simple AWS Lambda Function
# Lab link: https://learn.acloud.guru/handson/f2b58b6b-2a05-435a-8746-ca1ff25b9773

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt
    
    # pip install aws-cdk.aws-lambda
    
    # cdk bootstrap aws://001500016315/us-east-1
    
    # cdk ls (output:SimpleLambdaFunction)
        # (Go check the CloudFormation and there will be a stack called "SimpleLambdaFunction")
    
    # cdk deploy SimpleLambdaFunction
    
    # Answer deployed!
    
from aws_cdk.core import App, Construct
from aws_cdk import(
    aws_lambda as _lambda,
    core
    )

# Create a Lambda Function
class LambdaFunction(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        lambda_function = _lambda.Function(
            self,"mylambdafunction",
            function_name = "HelloWorld",
            runtime = _lambda.Runtime.PYTHON_3_8,
            code = _lambda.Code.asset("lambda"),
            handler = "lambda_function.lambda_handler"
        )
        

##  You may need to replace Function code:
## https://raw.githubusercontent.com/linuxacademy/content-lambda-deep-dive/master/section_2/live_act_1/lambda_function.py
    
##  You may need to replace the current test event code:
## https://raw.githubusercontent.com/linuxacademy/content-lambda-deep-dive/master/section_2/live_act_1/test_event.json