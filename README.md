Before starting to deploy answers, please run following commands:

///

python3 -m venv .env

source .env/bin/activate

pip install -r requirements.txt

pip install boto3

///

After that you can try "cdk ls" to list the stacks in the app

Try "cdk deploy xxx(stack name)" to deploys your answers!!