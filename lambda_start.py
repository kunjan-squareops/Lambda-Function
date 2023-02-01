## Start all stopped instances having 'testing' tag with value as 'tostart'.

import json
import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
def lambda_handler(event, context):
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']},{'Name': 'tag:testing','Values':['tostart']}])
    for instance in instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).start()
        print("Instance ID is started"+instance.id)
    return "success"
