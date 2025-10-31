# S3 Security Monitor

## Goals

- How to connect S3 -> Lambda -> CloudWatch for real-time detection
- How Lambda code inspects events and applies basic security logic
- How CloudWatch acts as your SOC log collector
- How AWS's event driven model mimics SIEM automation

## Scenario

You want to:

- Detect any unauthorized file types (e.g. .exe, .zip, .bat)
- Log every upload for auditing.
- (Later) Notify security if something looks dangerous.

Making AWS automatically check

## Architecture

```
User uploads file  →  S3 bucket event  
                     ↓
               AWS Lambda (our function)
                     ↓
          CloudWatch Logs (security record)
```


### Create S3 Bucket

1. Go to AWS Console -> S3 -> Create bucket
2. Name the bucket
3. Keep region the same as Lambda
4. Default settings are okay

### Create a Lambda Function

1. Go to AWS Lambda -> Create function
2. Choose
- Author from scratch
- Name: `S3SecurityMonitor`
- Runtime: Python 3.12
- Permissions: create or use existing role (default fine)
3. Create Function

### Connect S3 as a Trigger

Inside new functionL
1. Click `Add Trigger`
2. Choose S3
3. Select bucket
4. Event Type: All object create events
5. Leave prefix/suffix blank -> Add


### Write the Security Logic

In the Code editor replace the precode with this new code: 

```
import json

def lambda_handler(event, context):
    print("=== S3 Security Monitor Triggered ===")

    # Extract bucket and object info
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    size = event['Records'][0]['s3']['object'].get('size', 0)

    print(f"File uploaded: {key} in bucket: {bucket} (Size: {size} bytes)")

    # Define suspicious patterns
    suspicious_extensions = ('.exe', '.zip', '.bat', '.dll', '.scr')

    # Simple security logic
    if key.lower().endswith(suspicious_extensions):
        print(f"⚠️ ALERT: Suspicious file detected - {key}")
        status = "Suspicious"
    else:
        print(f"✅ Safe file uploaded - {key}")
        status = "Clean"

    # Return structured log
    return {
        'statusCode': 200,
        'body': json.dumps({
            'file': key,
            'bucket': bucket,
            'status': status,
            'size': size
        })
    }
```

ie.
<img width="1540" height="848" alt="image" src="https://github.com/user-attachments/assets/23489650-a7bb-4859-8630-ca8f740dab79" />


Click Deploy

### Testing

1. Uploading a normal file:

-> Creating a file Hello.txt
-> Uploading it 
-> Check Log Stream

<img width="1899" height="670" alt="image" src="https://github.com/user-attachments/assets/7fd7df25-4948-494e-9056-b6d23652c2e9" />

2. Uploading Malicious Fiel

- Creating a file virus.txt
-> Uploading it
-> Check Log Stream

<img width="1638" height="576" alt="image" src="https://github.com/user-attachments/assets/99ae0477-722c-4abe-91ec-d486cdf72dcf" />










