# AWS Automation Practice Script

This folder contains a small python script that interacts with AWS services using 
the `boto3` SDK

## IAM User Audit (`IAM_User_audit.py`)
**Purpose:**  
Checks all IAM users in your AWS account, lists their access keys, and identifies their key status (Active/Inactive).

**How It Works:**  
- Connects to AWS using an existing profile (e.g. `amplify-admin`)
- Uses the `boto3` IAM client
- Lists IAM users and their access keys
- Prints key ID (masked), age, and status

**Example Output:**
```bash
Checking IAM user access keys...

👤 amplify-admin | AKIA****OMGEN | 0 days old | Status: Inactive
👤 amplify-admin | AKIA****B5THG | 0 days old | Status: Active
👤 lotus-admin   | AKIA****JABA4 | 0 days old | Status: Active
------------------------------------------------------------
```

## Requirements

AWS CLI configured with valid profile
`boto3` installed 

```
pip install boto3
```
