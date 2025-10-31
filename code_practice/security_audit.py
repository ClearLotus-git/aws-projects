import boto3

session = boto3.Session(profile_name="amplify-admin")
s3 = session.client("s3")

response = s3.list_buckets()
for bucket in response["Buckets"]:
    bucket_name = bucket["Name"]
    location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    print(f"\n🔍 Checking {bucket_name} (Region: {location})")

    # Check if bucket is public
    acl = s3.get_bucket_acl(Bucket=bucket_name)
    for grant in acl['Grants']:
        grantee = grant.get('Grantee', {})
        if grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
            print(f"Bucket {bucket_name} is PUBLIC!")
            break
    else:
        print("Bucket is private.")
