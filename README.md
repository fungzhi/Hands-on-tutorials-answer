Get your answer with "git clone https://github.com/fungzhi/Hands-on-tutorials-answer.git"

Before starting to deploy answers, please check your CloudFormation Stacks 
and make sure there is no stacks were deployed from Hands-on-tutorials-answer before.
If yes, please delete the deployed stacks

Please run the following commands to get your answer(s):

///

cd Hands-on-tutorials-answer

python3 -m venv .env

source .env/bin/activate

pip install -r requirements.txt

///

Upgrade your CDK

///

sudo yum -y update

sudo yum -y install aws-cli

sudo -H pip install awscli --upgrade

python -m ensurepip --upgrade

python -m pip install --upgrade pip

python -m pip install --upgrade virtualenv

npm install -g aws-cdk@latest

which npm

npm install -g aws-cdk@latest --force

///

After that you can try "cdk ls" to list the stacks in the app

If stacks were shown, try "cdk deploy xxx(stack name)" to deploys your answers!!

Learn more about AWS CDK : https://docs.aws.amazon.com/cdk/latest/guide/home.html
