# Initialize a Local Amplify App

## Overview

Use AWS Amplify to configure a cloud backend for the app. AWS Amplify Gen 2 will be using 
a fullstack TypeScript developer experience for defining backends.

## Goals
- Set up Amplify Auth
- Set up Amplify Data
- Set up Amplify Storage


### Exercise

When the user signs up, they receive a verification email.

Set up auth resource: 

(Continuing using Gen1) 

1. Add an API and database:

```
amplify add api
```
When asked choose GraphQL -> enter when prompted questions

In the new schema `schemagraphql` paste over the following code to allow creator user read,edit,delete access:

```
# This "input" configures a global authorization rule to enable public access to
# all models in this schema. Learn more about authorization rules here: https://docs.amplify.aws/cli/graphql/authorization-rules
input AMPLIFY { globalAuthRule: AuthRule = { allow: public } } # FOR TESTING ONLY!

type Note @model @auth(rules: [{ allow: owner }]) {
  id: ID!
  name: String!
  description: String
  image: String
  owner: String
}
```

Save the file. Then deploy:

```
amplify push
| Fetching updates to backend environment: dev from the cloud.
⚠️  WARNING: your GraphQL API currently allows public create, read, update, and delete access to all models via an API Key. To configure PRODUCTION-READY authorization rules, review: https://docs.amplify.aws/cli/graphql/authorization-rules

√ Successfully pulled backend environment dev from the cloud.
- Building resource api/notesapp
⚠️  WARNING: your GraphQL API currently allows public create, read, update, and delete access to all models via an API Key. To configure PRODUCTION-READY authorization rules, review: https://docs.amplify.aws/cli/graphql/authorization-rules


    Current Environment: dev
    
┌──────────┬───────────────┬───────────┬───────────────────┐
│ Category │ Resource name │ Operation │ Provider plugin   │
├──────────┼───────────────┼───────────┼───────────────────┤
│ Api      │ notesapp      │ Create    │ awscloudformation │
└──────────┴───────────────┴───────────┴───────────────────┘
```


















