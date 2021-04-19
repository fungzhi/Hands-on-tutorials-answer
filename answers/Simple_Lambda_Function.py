#a cloud guru Hand on lab
# Creating a Simple AWS Lambda Function

# pip install aws-cdk.aws-lambda
# cdk bootstrap aws://001500016315/us-east-1
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
            self,"abc_test",
            function_name = "HelloWorld",
            runtime = _lambda.Runtime.PYTHON_3_6,
            code = _lambda.Code.asset("lambda"),
            handler = "lambda.lambda_handler"
        )