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






























