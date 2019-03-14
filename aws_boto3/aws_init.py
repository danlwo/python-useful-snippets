import boto3


def aws_init(aws_profile):
    global aws_session
    aws_session = boto3.Session(profile_name = aws_profile)
