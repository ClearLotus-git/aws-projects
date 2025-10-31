# Deploy and Host a React App

## Overview

Deploy a React single-page application using AWS Amplify’s Git-based CI/CD workflow,
connecting a GitHub repository for automated builds and global hosting on Amplify’s CDN, and demonstrating continuous deployment through version updates.

### Exercise

Create a new React Application

In a new termional window, use the following to use Vite to create a react application:

```
npm create vite@latest notesapp -- --template react

^^SNIP^^

 VITE v7.1.12  ready in 588 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

When finished view application in the web browser

In another terminal window run: 

```
cd notesapp
npminstall
npm run dev

^SNIP^\
> notesapp@0.0.0 dev
> vite

Port 5173 is in use, trying another one...

  VITE v7.1.12  ready in 265 ms

  ➜  Local:   http://localhost:5174/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

```

In github create a new repository named `notesapp`

Then, push the new repo by opening another termianl window, navigating to the app's root folder
and running the following commands:

```
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:<your-username>/notesapp.git
git branch -M main
```

Next, Install the Amplify Packages: 

Configure local repo: 

```
npm create amplify@latest -y
```

In the console deploy the notesapp:

<img width="1916" height="778" alt="image" src="https://github.com/user-attachments/assets/2edc01d7-a41d-4e2a-afa2-23c005ee9399" />

Automatically deploying code changes looks like this:

Using text editior update the application code by navigating to the notesapp/src/App.jsx file.. with the following code: 

```
import reactLogo from "./assets/react.svg";
import "./App.css";
function App() {
 return (
 <div className="App">
 <header className="App-header">
 <img src={reactLogo} className="logo react" alt="React logo" />
 <h1>Hello from Amplify</h1>
 </header>
 </div>
 );
}
export default App;
```

<img width="1031" height="405" alt="image" src="https://github.com/user-attachments/assets/66c634d3-1a10-47b4-b8b2-22f0ddba9887" />

Push code changes:

```
git add .
git commit -m 'changes for amplify'
git push origin main

^SNIP^
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 6 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 510 bytes | 510.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: This repository moved. Please use the new location:
remote:   https://github.com/ClearLotus-git/notesapp.git
To https://github.com/clearlotus-git/notesapp.git
   3dbf6ea..cedcaaf  main -> main
```

Update your deployed application:

<img width="1903" height="776" alt="image" src="https://github.com/user-attachments/assets/2b896b85-7b65-496f-8113-93d1530b8caf" />

Change to website after: 

<img width="740" height="527" alt="image" src="https://github.com/user-attachments/assets/4c658ec8-1681-497e-ad99-d3cc43dbbbe6" />


The React application in the AWS Cloud hass been deployed by integrating with GitHub and using AWS
Amplify.






