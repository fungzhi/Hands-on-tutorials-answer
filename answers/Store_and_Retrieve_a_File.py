# Hands-on Lab: Store and Retrieve a File
# Tutorial link: https://aws.amazon.com/getting-started/hands-on/backup-files-to-amazon-s3/

# This is the answer of Hands-on Tutorial: Store and Retrieve a File

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate

    # pip install boto3

    # python -m pip install aws-cdk.aws-s3
    
    # cdk ls    (output: StoreAndRetrieveFile)
        #(Go check the CloudFormation and there will be a stack called "StoreAndRetrieveFile")
    
    # cdk deploy StoreAndRetrieveFile
    
    # Answer deployed!


from aws_cdk import (aws_s3 as s3, core)
import boto3

class S3Bucket(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
        #create an S3 bucket
        myBucket = s3.Bucket(self,
                             'MyFirstBucket',
                             # Change "yourBucket" to your bucket before deploying answers //
                             bucket_name='yourbucket',
                             )

# After deploying upper codes
# Please delete """ """ to available the following codes
# Now deploy "StoreAndRetrieveFile" again
"""
#upload an S3 file
s3_resource = boto3.resource('s3')
s3_resource.meta.client.upload_file(
    Filename='answers/cat.jpg',
    Bucket='yourbucket',
    Key='cat.jpg')
"""