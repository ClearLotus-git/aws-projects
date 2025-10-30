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










