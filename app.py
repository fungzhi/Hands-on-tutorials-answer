#!/usr/bin/env python3

import os
from aws_cdk import core


from answers.build_a_static_website_with_amazon_s3 import StaticWebsiteBucket
from answers.create_an_audio_transcript import S3Template
from answers.create_and_query_a_nosql_table import CreateTable, InputData, QueryData
from answers.Creating_Virtual_Private_Cloud_Activity import CreateVPC
from answers.Filter_Messages_Published_to_Topics import CreateSNSSQS
from answers.introduction_to_aws_identity_and_access_management import IAM
from answers.Store_and_Retrieve_a_File import S3Bucket
#from answers.send_messages_between_distributed_applications import CreateQueue, SendMessages
# Tentative Draft Version
# from marking.creating_an_amazon_cloudfront_distribution import CloudFrontWebSite
#from answers.create_an_audio_transcript import Transcriptfile
from answers.Create_EC2_Instance import ec2Stack
#from answers.Create_Security_Group import sgStack


env = core.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region="us-east-1")

app = core.App()
StaticWebsiteBucket(app, "BuildStaticWebsiteWithAmazonS3", env=env)
S3Template(app, "CreateAnAudioTranscript", env=env)
CreateTable, InputData, QueryData(app, "CreateAndQueryNoSQLTable", env=env)
CreateVPC(app, "CreatingVirtualPrivateCloudActivity", env=env)
CreateSNSSQS(app, "FilterMessagesPublishedtoTopics", env=env)
IAM(app, "IntroductionToAwsIdentityAndAccessManagement", env=env)
S3Bucket(app, "StoreAndRetrieveFile", env=env)
ec2Stack(app, "CreateEC2Instance", env=env)
#sgStack(app, "CreateSecurityGroup", env=env)
# Tentative Draft Version
# CreateQueue, SendMessages, CreateTable, InputData, QueryData, StaticWebsiteBucket, CloudFrontWebSite, IAM(app, "marking")
#CreateQueue, SendMessages(app, "CreateSNSSQS", env=env)
#Transcriptfile(app, "Transcriptfile", env=env)


app.synth()
