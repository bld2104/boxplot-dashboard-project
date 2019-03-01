# boxplot

**Table of contents**

- [Environment](#environment)
  - [AWS Credentials](#aws-credentials)
- [Working flow](#working-flow)
  - [Write the lambda](#write-the-lambda)
  - [Deploy](#deploy)
- [API Gateway](#api-gateway)

## Environment

### [Apex](http://apex.run/)
For deployment we are using apex tool.

[Installation](https://github.com/apex/apex/blob/master/docs/installation.md):
```sh
curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh
```

### AWS Credentials
1. AWS Credentials is required for deploy via Apex.
Getiing `aws_access_key_id` and `aws_secret_access_key`:
    1. Open the **IAM console**.
    1. In the navigation panel, choose **Users**.
    1. Choose **Apex** user
    1. Choose the **Security Credentials** tab and then choose **Create Access Key**.
    1. Then save `aws_access_key_id` and `aws_secret_access_key` it is required for the next step.

1. Create `credentials` and `config` files in the home directory.

`~/.aws/credentials`:
```sh
[apex]
aws_access_key_id=xxxxxxxxxxx
aws_secret_access_key=xxxxxxxxxxxxxxxxxxx
```
`~/.aws/config`:
```sh
[profile apex]
output=json
region=us-east-1
```

## Workflow

### Write the lambda
Let's create a simple lambda and deploy it.

All the main points of lambdas should be located at:
```
./functions/<lambdaName>/src/[filename].[extention]
```

Create a new lambda named **helloWorld**.

`functions/helloWorld/src/main.py`:
```js
def handler():
  print("Hello World!")
```

### Deploy

Let's [deploy](https://github.com/apex/apex/blob/master/docs/deploy.md) this lambda via apex.
```sh
apex deploy helloWorld
```
We will see the real name and the lambda alias:
```
• creating function         env= function=helloWorld
• created alias current     env= function=helloWorld version=14
• function created          env= function=helloWorld name=boxplot_helloWorld version=14
```

## API Gateway

*You can initiate API Gateway structure by:*

1. Navigate to API Gateway in [AWS console](https://console.aws.amazon.com/apigateway)
2. Create or select API
3. Select `Resources` -> `Actions` -> `Import API`
4. Load `api-gateway-swagger.json` file from thr root of the project

