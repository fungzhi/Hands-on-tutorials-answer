# This is the answer of Hands-on Tutorial: Create an Audio Transcript
# Tutorial link: https://aws.amazon.com/getting-started/hands-on/create-audio-transcript-transcribe/?nc1=h_ls

    # cd Hands-on-tutorials-answer
    
    # python3 -m venv .env
    
    # source .env/bin/activate
    
    # pip install -r requirements.txt
    
    # cdk ls   (output: CreateAnAudioTranscript)

    # cdk deploy CreateAnAudioTranscript (go check the CoudFormation and there will be a stack called "CreateAnAudioTranscript", check S3 it will create a bucket called 'create-an-audio-transcript')
    
    # delete lines 45, 51, 55 and 66 ["""]
    
    # cdk deploy CreateAnAudioTranscript again (go check S3 bucket it will uploap an mp3 file and upload it to transcribe jobs)
    
    # Answer deployed!

    # To prevent effects other answers, please remember to delete the transcribe jobs, S3 bucket, "CreateAnAudioTranscript" stack and add ["""] again in lines 45, 51, 55, 66 after checking the answer

from aws_cdk import (aws_s3 as s3, core)
import time
import boto3

class S3Template(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
        #create an S3 bucket
        #The bucker name can be reused for student accounts until a personal account is registered, if you need to change bucker name, pleace change lines 35, 49, 58 bucket name together)
        myBucket = s3.Bucket(self,
                             'MyFirstBucket',
                             bucket_name='create-an-audio-transcript',
                             public_read_access= True,
                             )

app = core.App()
S3Template(app, "S3Template", env={'region': 'us-east-1'})
app.synth()


#upload an S3 file
"""
s3_resource = boto3.resource('s3')
s3_resource.meta.client.upload_file(
    Filename='answers/transcribe-sample.mp3',
    Bucket='create-an-audio-transcript',
    Key='transcribe-sample.mp3')
"""


#upload S3 file to transcribe
"""
transcribe = boto3.client('transcribe')
job_name = "sample-transcription-job"
job_uri = "s3://create-an-audio-transcript/transcribe-sample.mp3"
class Transcriptfile(core.Stack):
    transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='en-US'
)
"""