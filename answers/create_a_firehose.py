# Lab: Create A Firehose

# This is the answer of Hands-on Tutorial: Create A Firehose

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt ( aws-cdk.aws-kinesisfirehose )
    
    # cdk ls   (Output: FirehoseDeliveryStream)
    
    # cdk deploy FirehoseDeliveryStream
        # (Go check the CloudFormation and there will be a stack called "FirehoseDeliveryStream")
    
# Answer deployed!
from aws_cdk import (
    core,
    aws_kinesisfirehose as firehose,
    aws_s3 as s3,
    aws_iam as iam
)

class CreateFirehose(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

    # Step 1: Create a new S3 bucket for Firehose
        # Create Bucket
        bucket = s3.Bucket(self, "cdk-firehose-bucket")

    # Step 2: Create a new IAM policy with name "FirehosePolicy"
        # Select "Kinesis" and than select "Firehose"
        # Add "AmazonS3FullAccess" of policy
        # Enter "FirehosePolicy" of a IAM role
        
        # IAM Role for Firehose
        firehose_role = iam.Role(self, "FirehoseRole",
            assumed_by = iam.ServicePrincipal(
                service = "firehose.amazonaws.com"
            )
        )


        delivery_policy = iam.Policy(
            self, "FirehosePolicy",
            policy_name = "FirehosePolicy",
            statements = [
                iam.PolicyStatement(
                    effect = iam.Effect.ALLOW,
                    actions = ["s3:*"],
                    resources = ["*"]
                )
            ]               
        )

        delivery_policy.attach_to_role(firehose_role)

    # Step 3: Create a new Firehose delivery stream with name "TestStrem"
        # Enter the Amazon Kinesis Console
        # Select Delivery streams in Amazon Kinesis
        # Create a Delivery Stream
            # Enter "TestStream" of a delivery stream
            # Choose Amazon S3 destination
                # Choose to connect your S3 bucket when you created
            # Choose Amazon IAM Permissions
                # Select to 'Choose existing IAM role'
                # Select "FirehosePolicy" of the existing IAM role
        # Next utill to Create a Delivery Stream
    
        # Firehose Delivery Stream
        delivery_stream = firehose.CfnDeliveryStream(
            self, "TestStream",
            delivery_stream_name = "TestStream",
            s3_destination_configuration = {
                "bucketArn": bucket.bucket_arn,
                "roleArn": firehose_role.role_arn
            },
            elasticsearch_destination_configuration = None
        )

        # delivery_stream.add_depends_on(firehose_role)

        # We assign the stream's arn and name to a local variable for the Object.
        self._delivery_stream_name = delivery_stream.delivery_stream_name
        self._delivery_stream_arn = delivery_stream.attr_arn
    
    # Using the property decorator to export value delivery_arn
    @property
    def main_delivery_stream_props(self):
        return self._delivery_stream_name, self._delivery_stream_arn

#  You may delete your stack(FirehoseDeliveryStream) to clean up your environment

    # cdk destroy FirehoseDeliveryStream
        # (Go check the CloudFormation a stack called "FirehoseDeliveryStream" will be destroyed)

# Clean up finished!