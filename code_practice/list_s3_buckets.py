import boto3

session = boto3.Session(profile_name="amplify-admin")
s3 = session.client("s3")

response = s3.list_buckets()

print("Your S3 Buckets:\n")
for bucket in response["Buckets"]:
    print(f"- {bucket['Name']} (Created: {bucket['CreationDate']})")
