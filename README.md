Get your answer with "git clone https://github.com/fungzhi/Hands-on-tutorials-answer.git"

Before starting to deploy answers, please run following commands:

///

cd Hands-on-tutorials-answer

python3 -m venv .env

source .env/bin/activate

pip install -r requirements.txt

///

After that you can try "cdk ls" to list the stacks in the app

If stacks were shown, try "cdk deploy xxx(stack name)" to deploys your answers!!

Learn more about AWS CDK : https://docs.aws.amazon.com/cdk/latest/guide/home.html
