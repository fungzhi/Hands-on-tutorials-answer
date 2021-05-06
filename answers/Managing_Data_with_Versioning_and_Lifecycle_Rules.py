# A Cloud Guru Hand on lab: Managing Data in S3 with Versioning and Lifecycle Rules
# Lab link: https://learn.acloud.guru/handson/9366814c-d237-4e04-9b64-e7c4e0cf1884

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt
    
    # pip install aws_cdk.aws_s3
    
    # pip install aws_cdk.aws_s3_deployment
    
    # cdk ls (output:VersioningAndLifecycleRules)
        # (Go check the CloudFormation and there will be a stack called "VersioningAndLifecycleRules)")
    
    # cdk deploy VersioningAndLifecycleRules
    
    # Answer deployed!

from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    core,
    )


class LifecycleRuleBucket(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
        
        #Create an S3 bucket, Enable versioning, Assign a Lifecycle Rule
        bucket = s3.Bucket(self,
            id = "lifecyclerulebucket", 
            bucket_name = "versiong-and-lifecycle-rule-bucket", 
            versioned = True,
            lifecycle_rules = [
                s3.LifecycleRule(
                    id = "image-rule",
                    prefix = "Images",
                    transitions = [
                        s3.Transition(
                        storage_class = s3.StorageClass.ONE_ZONE_INFREQUENT_ACCESS,
                        transition_after = core.Duration.days(30))
                        ]    
                    ) 
            ]
        )
        
        #Create Folder and upload one object
        s3_deployment.BucketDeployment(self, "Deployment",
            sources = [s3_deployment.Source.asset("./Images")],
            destination_bucket = bucket,
            destination_key_prefix = "Images"
        )