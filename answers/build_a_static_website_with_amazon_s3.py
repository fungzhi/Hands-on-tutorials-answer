# AWS Educate Lab: Build a Static Website with Amazon S3 Activity
# Activity Link: https://www.awseducate.com/educator/s/content-view?id=static_website_s3_activity

# This is the answer of Hands-on Tutorial: Build a Static Website with Amazon S3 Activity

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt ( aws-cdk.aws-s3 aws-cdk.aws-s3-deployment )
    
    # cdk ls (Output: StaticWebsiteBucket)
    
    # cdk deploy StaticWebsiteBucket
        # (Go check the CloudFormation and there will be a stack called "StaticWebsiteBucket")
    
# Answer deployed!

from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_s3_deployment as s3_deploy 
)


class CreateWebsiteBucket(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an Amazon S3 Bucket
        bucket = s3.Bucket(self, "cdk-Static-Website-Bucket",
        # Upload Static Website Items in an Amazon S3 Bucket: "index.html", "bitbangers.png"
            website_index_document = "index.html" and "bitbangers.png",
            removal_policy = core.RemovalPolicy.DESTROY,
            public_read_access = True
        )
        
        # [Optional] Create a File in an Amazon S3 Bucket: "AWSEducateS3"
            # Static Website Items will be inside
        s3_deploy.BucketDeployment(self, "DeployWebsite",
            sources = [s3_deploy.Source.asset("./AWSEducateS3")],
            destination_bucket = bucket,
            destination_key_prefix = "AWSEducateS3"
        )

#  You may delete your stack(StaticWebsiteBucket) to clean up your environment

    # cdk destroy StaticWebsiteBucket
        # (Go check the CloudFormation a stack called "StaticWebsiteBucket" will be destroyed)

# Clean up finished!