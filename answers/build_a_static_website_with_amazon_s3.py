# AWS Educate Lab: Build a Static Website with Amazon S3 Activity
# Activity Link: https://www.awseducate.com/educator/s/content-view?id=static_website_s3_activity

from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_s3_deployment as s3_deploy 
)


class StaticWebsiteBucket(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create Bucket
        bucket = s3.Bucket(self, "cdk-Static-Website-Bucket",
            website_index_document = "hello-world.html",
            website_error_document = "error.html",
            removal_policy = core.RemovalPolicy.DESTROY,
            public_read_access = True
        )
        
        # Upload Static Website
        s3_deploy.BucketDeployment(self, "DeployWebsite",
            sources = [s3_deploy.Source.asset("./site-contents")],
            destination_bucket = bucket,
            destination_key_prefix = "site-contents"
        )
