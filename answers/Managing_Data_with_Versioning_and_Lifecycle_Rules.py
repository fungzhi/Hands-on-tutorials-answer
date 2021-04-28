# pip install aws_cdk.aws_s3
# pip install aws_cdk.aws_s3_deployment

from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    core,
    )


class LifecycleRuleBucket(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
        
        #Create an S3 bucket
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
        
        
        s3_deployment.BucketDeployment(self, "Deployment",
            sources = [s3_deployment.Source.asset("./Images")],
            destination_bucket = bucket,
            destination_key_prefix = "Images"
        )