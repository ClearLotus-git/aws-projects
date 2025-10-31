# Task 1: Create a Web App
Deploy static resources for your web application using the AWS Amplify Console.

## Step 1: Create the app

In a new terminal or command line window, run the following command to use Vite to create a React application:


```
npm create vite@latest profilesapp -- --template react
cd profilesapp
npm install
npm run dev
```

In vscode:

```
npm create vite@latest profilesapp -- --template react

^SNIP^

◇  Starting dev server...

> profilesapp@0.0.0 dev
> vite

Port 5173 is in use, trying another one...
Port 5174 is in use, trying another one...

  VITE v7.1.12  ready in 363 ms

  ➜  Local:   http://localhost:5175/   <--------
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

In new termianl inside vscode same directory:

```
 cd .\profilesapp\
projects\basic_webapp\profilesapp> ls


    Directory: C:\Users\Nick\projects\basic_webapp\profilesapp


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        10/31/2025  12:40 PM                node_modules
d-----        10/31/2025  12:39 PM                public
d-----        10/31/2025  12:39 PM                src
-a----        10/30/2025   4:45 PM            253 .gitignore
-a----        10/30/2025   4:45 PM            763 eslint.config.js
-a----        10/31/2025  12:39 PM            360 index.html
-a----        10/31/2025  12:40 PM          97833 package-lock.json
-a----        10/31/2025  12:39 PM            608 package.json
-a----        10/30/2025   4:45 PM           1157 README.md
-a----        10/30/2025   4:45 PM            161 vite.config.js
```

```
projects\basic_webapp\profilesapp> npm install

added 46 packages, and audited 202 packages in 893ms

32 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

```
PS C:\Users\Nick\projects\basic_webapp\profilesapp> npm run dev

> profilesapp@0.0.0 dev
> vite


  VITE v7.1.12  ready in 264 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

```

## Step 2: Install the Amplify packages

In github create a new repository called `profilesapp` and make sure the permissions are public -> create

<img width="1443" height="741" alt="image" src="https://github.com/user-attachments/assets/aeeef876-8795-43c4-8345-bd537014101e" />

In vscode in the root repository as before use the above commands:

```
echo "# profilesapp" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ClearLotus-git/profilesapp.git
git push -u origin main
```

Output ending should look like: 

```
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/ClearLotus-git/profilesapp.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\Nick\projects\basic_webapp> 
```


## Step 3: Initialize a GitHub repository

In a new terminal (same directory root) run the following: 

```
npx create amplify@latest -y
```

```
1:40:02 PM Installing devDependencies:
1:40:02 PM  - @aws-amplify/backend
1:40:02 PM  - @aws-amplify/backend-cli
1:40:02 PM  - aws-cdk-lib@2.204.0
1:40:02 PM  - constructs@^10.0.0
1:40:02 PM  - typescript@^5.0.0
1:40:02 PM  - tsx
1:40:02 PM  - esbuild

1:40:02 PM Installing dependencies:
1:40:02 PM  - aws-amplify

1:40:02 PM ✔ 1:44:01 PM DevDependencies installed
1:44:01 PM ✔ 1:44:45 PM Dependencies installed
1:44:45 PM ✔ 1:44:45 PM Template files created
1:44:46 PM Successfully created a new project!

1:44:46 PM Welcome to AWS Amplify!
1:44:46 PM  - Get started by running npx ampx sandbox.
1:44:46 PM  - Run npx ampx help for a list of available commands.

1:44:46 PM Amplify collects anonymous telemetry data about general usage of the CLI. Participation is optional, and you may opt-out by using npx ampx configure telemetry disable. To learn more about telemetry, visit https://docs.amplify.aws/react/reference/telemetry

$ projects\basic_webapp>
```

Push the changes:

```
git add .
git commit -m 'installing amplify'
git push origin main

^SNIP^
Enumerating objects: 31, done.
Counting objects: 100% (31/31), done.
Delta compression using up to 6 threads
Compressing objects: 100% (25/25), done.
Writing objects: 100% (30/30), 225.64 KiB | 5.25 MiB/s, done.
Total 30 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/ClearLotus-git/profilesapp.git
   ac58798..6f89081  main -> main
```

## Step 4: Deploy your app with AWS Amplify

Amplify -> `Create new app` -> Select repository connected to github -> `Deploy`

<img width="1577" height="659" alt="image" src="https://github.com/user-attachments/assets/f99e15e7-b6b0-4dc4-b3c4-8c81839c108c" />


Issue: Deploy succeeded but React app isnt rendering

check src codes
```
$ basic_webapp\profilesapp> npm run build

> profilesapp@0.0.0 build
> vite build

vite v7.1.12 building for production...
✓ 32 modules transformed.
dist/index.html                   0.46 kB │ gzip:  0.29 kB
dist/assets/react-CHdo91hT.svg    4.13 kB │ gzip:  2.05 kB
dist/assets/index-COcDBgFa.css    1.38 kB │ gzip:  0.70 kB
dist/assets/index-DwNzZMGt.js   195.25 kB │ gzip: 61.13 kB
✓ built in 1.64s
PS C:\Users\Nick\projects\basic_webapp\profilesapp> 
```

amplify.yml needs to be created here: 

```
$ \projects\basic_webapp


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        10/31/2025   1:44 PM                amplify
d-----        10/31/2025   1:44 PM                node_modules
d-----        10/31/2025   1:59 PM                profilesapp
-a----        10/31/2025   1:44 PM             76 .gitignore
-a----        10/31/2025   1:44 PM        1452042 package-lock.json
-a----        10/31/2025   1:44 PM            921 package.json
-a----        10/31/2025  12:48 PM             32 README.md
```

amplify.yaml

```
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - cd profilesapp
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: profilesapp/dist
    files:
      - '**/*'
  cache:
    paths:
      - profilesapp/node_modules/**/* 
```

Redeploy app:

```
amplify init
amplify hosting add
amplify publish
```







