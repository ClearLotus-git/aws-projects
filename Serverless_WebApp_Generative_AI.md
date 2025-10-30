# Build a Serverless Web Application using Generative AI

## Overview

In this tutorial, you will learn how to use AWS Amplify to build a serverless web application powered by Generative AI using Amazon Bedrock and the Claude 3 Sonnet foundation model. Users can enter a list of ingredients, and the application will generate delicious recipes based on the input ingredients. The application includes an HTML-based user interface for ingredient submission and a backend web app to request AI-generated recipes.


<img width="873" height="349" alt="image" src="https://github.com/user-attachments/assets/682c7551-88c2-48e8-81f6-67eac5d0a2c0" />

---

### Task 1 - Configure AWS Amplify to host your frontend application with continuous deployment built in


#### Step 1 - Create a new React application

In VScode or powershell command prompt of choice: 

```
npm create vite@latest ai-recipe-generator -- --template react-ts -y

◇  Starting dev server...

> ai-recipe-generator@0.0.0 dev
> vite


  VITE v7.1.12  ready in 1634 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help


```

```
cd ai-recipe-generator
npm install
npm run dev


> ai-recipe-generator@0.0.0 dev
> vite


  VITE v7.1.12  ready in 271 ms

  ➜  Local:   http://localhost:5173/   <--------- 
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

```
<img width="1906" height="842" alt="image" src="https://github.com/user-attachments/assets/3f1b09df-84d6-46df-9e27-028f6faee97d" />


#### Step 2 - Initialize a GitHub repository

Create new repository in github named  `ai-recipe-generator`

Intialize Git and COnnect to Github

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ClearLotus-git/ai-recipe-generator.git
git push -u origin main
```

Issue 
`Permission denied (publickey)`

Fix: switched remote to HTTPS and reauthenticated via browser.

Merge Conflict Resolution

```
git pull origin main --allow-unrelated-histories
# conflict in README.md resolved manually
git add README.md
git commit -m "Resolved README conflict"
git push -u origin main
```

Repository successfully pushed and synced with GitHub.

<img width="993" height="747" alt="image" src="https://github.com/user-attachments/assets/e97300fc-da7c-48c8-865c-55a1eea43676" />

#### Step 3: Install the Amplify packages

```
\ai-recipe-generator> npm install -g @aws-amplify/cli

added 79 packages in 1m

24 packages are looking for funding
  run `npm fund` for details
```

```
\ai-recipe-generator> amplify -v
14.2.0
```

Running this will send to browser sign in to Aws

```
PS C:\Users\Nick\projects\ai-recipe-generator> amplify configure
Follow these steps to set up access to your AWS account:

Sign in to your AWS administrator account:
https://console.aws.amazon.com/
Press Enter to continue

Specify the AWS Region
? region:  (Use arrow keys)
> us-east-1 
  us-east-2 
  us-west-1 
  us-west-2 
  eu-north-1 
  eu-south-1 
  eu-west-1 
(Move up and down to reveal more choices)
```

<img width="943" height="794" alt="image" src="https://github.com/user-attachments/assets/e2ac19e0-dd95-4fcb-97c8-e2e63fb5695a" />

<img width="1196" height="490" alt="image" src="https://github.com/user-attachments/assets/dd60e703-b0f9-483f-b8d9-93eb1bfacd3c" />

<img width="1911" height="712" alt="image" src="https://github.com/user-attachments/assets/26bf6739-1780-47dd-9e26-9ad20112eb44" />

<img width="802" height="868" alt="image" src="https://github.com/user-attachments/assets/7b8abde9-eea9-4935-825f-e12761f23613" />

<img width="561" height="628" alt="image" src="https://github.com/user-attachments/assets/62ff218a-aa62-4e7d-8b9d-e174cc257070" />

<img width="1897" height="662" alt="image" src="https://github.com/user-attachments/assets/e5eee5d9-b9d2-4e83-a7b6-72f975466757" />

<img width="1275" height="853" alt="image" src="https://github.com/user-attachments/assets/679ffe4f-0542-4b99-b597-4b87471ed69c" />

<img width="1501" height="843" alt="image" src="https://github.com/user-attachments/assets/ebd58051-b9f0-4f1d-8732-3a342cffa827" />

<img width="1505" height="850" alt="image" src="https://github.com/user-attachments/assets/81400ab3-583f-4a7a-a027-ed15fb4d41b8" />


### Task 2 - Manage Users

Configure an authentication resource for the app using AWS Amplify Auth, powered by Amazon Cognito. 
Cognito is a powerful user directory service that manages user registration, authentication, account recovery, and more.
Use the AWS Management Console to enable access to Amazon Bedrock and Claude 3 Sonnet foundation model, which the app will use to generate recipes.

#### Step 1 -  Set up Amplify Auth

```
\ai-recipe-generator> amplify init
⚠️ For new projects, we recommend starting with AWS Amplify Gen 2, our new code-first developer experience. Get started at https://docs.amplify.aws/react/start/quickstart/
√ Do you want to continue with Amplify Gen 1? (y/N) · yes
√ Why would you like to use Amplify Gen 1? · Prefer not to answer
Note: It is recommended to run this command from the root of your app directory
? Enter a name for the project airecipegenerator
The following configuration will be applied:

Project information
| Name: airecipegenerator
| Environment: dev
| Default editor: Visual Studio Code
| App type: javascript
| Javascript framework: react
| Source Directory Path: src
| Distribution Directory Path: build
| Build Command: npm.cmd run-script build
| Start Command: npm.cmd run-script start

? Initialize the project with the above configuration? Yes
Using default provider  awscloudformation
? Select the authentication method you want to use: (Use arrow keys)
> AWS profile 
AWS access keys
```

```
? Initialize the project with the above configuration? Yes
Using default provider  awscloudformation
? Select the authentication method you want to use: AWS profile
AWS access credentials can not be found.
? Setup new user Yes
Follow these steps to set up access to your AWS account:

Sign in to your AWS administrator account:
https://console.aws.amazon.com/
Press Enter to continue
```

Created new user with amplify privileges


<img width="1651" height="469" alt="image" src="https://github.com/user-attachments/assets/cc713b60-06a1-45f6-a26a-14856402426a" />

<img width="1248" height="372" alt="image" src="https://github.com/user-attachments/assets/3111d2a8-aab0-4037-83b4-d32270ef851c" />

<img width="1632" height="700" alt="image" src="https://github.com/user-attachments/assets/69053eb6-039c-4e09-add5-71cb53f9f757" />

<img width="1602" height="666" alt="image" src="https://github.com/user-attachments/assets/a19d94c2-aee7-49d5-8e05-2f298cd284a7" />

<img width="1160" height="740" alt="image" src="https://github.com/user-attachments/assets/d2b678fd-a93d-412e-8b8f-eb5a042a7035" />

<img width="1179" height="525" alt="image" src="https://github.com/user-attachments/assets/90463b1b-7ec9-4652-8ed0-c38c48d48aae" />


```
\projects\ai-recipe-generator> aws configure --profile amplify-admin
AWS Access Key ID [****************APEC]: 
AWS Secret Access Key [****************d+OX]: 
Default region name [us-east-1]: 
Default output format [json]: 
PS C:\Users\Nick\projects\ai-recipe-generator> aws sts get-caller-identity --profile amplify-admin
{
    "UserId": "ACCESS_KEY",
    "Account": "XXXXXXXXXXXX",
    "Arn": "arn:aws:iam::XXXXXXXXXXXXX:user/amplify-admin"
}

\projects\ai-recipe-generator> 
```

```
\ai-recipe-generator> amplify init
⚠️ For new projects, we recommend starting with AWS Amplify Gen 2, our new code-first developer experience. Get started at https://docs.amplify.aws/react/sttart/quickstart/
√ Do you want to continue with Amplify Gen 1? (y/N) · yes
√ Why would you like to use Amplify Gen 1? · Prefer not to answer
Note: It is recommended to run this command from the root of your app directory
? Enter a name for the project airecipegenerator
The following configuration will be applied:

Project information
| Name: airecipegenerator
| Environment: dev
| Default editor: Visual Studio Code
| App type: javascript
| Javascript framework: react
| Source Directory Path: src
| Distribution Directory Path: build
| Build Command: npm.cmd run-script build
| Start Command: npm.cmd run-script start

? Initialize the project with the above configuration? Yes
Using default provider  awscloudformation
? Select the authentication method you want to use: AWS access keys
? accessKeyId:  ********************
? secretAccessKey:  ****************************************
? region:  us-east-1
Adding backend environment dev to AWS Amplify app: d39jdyq2vvn2ky

Deployment completed.
Deploying root stack airecipegenerator [ ==========------------------------------ ] 1/4
        DeploymentBucket               AWS::S3::Bucket                CREATE_COMPLETE                Thu Oct 30 2025 18:55:52…
        AuthRole                       AWS::IAM::Role                 CREATE_IN_PROGRESS             Thu Oct 30 2025 18:55:37…
        UnauthRole                     AWS::IAM::Role                 CREATE_IN_PROGRESS             Thu Oct 30 2025 18:55:38…

√ Help improve Amplify CLI by sharing non-sensitive project configurations on failures (y/N) · no

    You can always opt-in by running "amplify configure --share-project-config-on"
Deployment state saved successfully.
√ Initialized provider successfully.
✅ Initialized your environment successfully.
✅ Your project has been successfully initialized and connected to the cloud!
Some next steps:

"amplify status" will show you what you've added already and if it's locally configured or deployed
"amplify add <category>" will allow you to add features like user login or a backend API
"amplify push" will build all your local backend resources and provision it in the cloud
"amplify console" to open the Amplify Console and view your project status
"amplify publish" will build all your local backend and frontend resources (if you have hosting category added) and provision it in the cloud


Pro tip:
Try "amplify add api" to create a backend API and then "amplify push" to deploy everything
```

```
\projects\ai-recipe-generator> amplify add auth
Using service: Cognito, provided by: awscloudformation
 
 The current configured provider is Amazon Cognito. 
 
 Do you want to use the default authentication and security configuration? Default configuration
 Warning: you will not be able to edit these selections. 
 How do you want users to be able to sign in? Username
 Do you want to configure advanced settings? No, I am done.
✅ Successfully added auth resource airecipegenerator29dd27b7 locally

✅ Some next steps:
"amplify push" will build all your local backend resources and provision it in the cloud
"amplify publish" will build all your local backend and frontend resources (if you have hosting category added) and provision it in the cloud
```

GO to `ai-recipe-generator\amplify\backend\auth\airecipegenerator29dd27b7/cli-inputs.json`   and edit the code (note im using gen1)

Change:
```
"emailVerificationSubject": "Your verification code",
"emailVerificationMessage": "Your verification code is {####}",
```
To:

```
"emailVerificationSubject": "Welcome to the AI-Powered Recipe Generator!",
"emailVerificationMessage": "Use this code to confirm your account: {####}"
```

amplify push 

<img width="994" height="484" alt="image" src="https://github.com/user-attachments/assets/22673051-d03c-4f4c-bb1d-7f4ac4cbc14f" />

Test it 

Edit main.tsx

```
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
// @ts-ignore
import awsExports from './aws-exports'



// 🔹 Import Amplify
import { Amplify } from 'aws-amplify'
import awsExports from '../amplify/aws-exports'

// 🔹 Configure Amplify with your backend setup
Amplify.configure(awsExports)

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

Edit App.tsx 

```
import { Authenticator } from '@aws-amplify/ui-react'
import '@aws-amplify/ui-react/styles.css'

export default function App() {
  return (
    <Authenticator>
      {({ signOut, user }) => (
        <main style={{ textAlign: 'center', marginTop: '50px' }}>
          <h1>Welcome to the AI-Powered Recipe Generator!</h1>
          <p>Hello, {user?.username}</p>
          <button onClick={signOut}>Sign out</button>
        </main>
      )}
    </Authenticator>
  )
}
```



Navigate to AWS management console --> Amazon Cognito --> User pools 

<img width="1912" height="624" alt="image" src="https://github.com/user-attachments/assets/71412a7c-ae66-433e-a951-f53e8824c4b3" />






