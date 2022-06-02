# lambdaStockGuru

lambdaStockGuru is a lambda to help monitor your stocks.

## Installation

Run this project in its own virtual environment. Look into venv or pyenv.
**Make sure you are in the root directory of application.**

You need to install the AWS CDK toolkit

```bash
npm install aws-cdk
```

You also need to pip install software from requirements.txt.

```bash
pip install -r requirements.txt
```

AND also pip install software from requirements.txt to package to be used in lambda

```bash
pip install --target=package -r requirements.txt
```

## Creation

You will need to create a Secret in AWS with following keys and values:

```json
{
  "HISTORY_APIURL_KEY": "Your_API_key",
  "DAYSAGO": 5,
  "HISTORY_APIURL": "https://api.finage.co.uk/history/stock/open-close"
}
```

Learn how to [create a Secret](https://aws.amazon.com/blogs/networking-and-content-delivery/securing-and-accessing-secrets-from-lambdaedge-using-aws-secrets-manager/)

## Running project locally

- In a terminal run

```bash
python lambdaFolder/stockGuru.py
```

## Deploying project to aws lambda

First, comment out imports under `Used for testing locally`. Then, uncomment imports under `Used for lambda`

- In a terminal run

```bash
cdk synth
cdk bootstrap
cdk deploy
```

**If lambda was deployed successfully and you can't find it, make sure your region in the UI is the same region in .aws/config**

- When done running lambda, run

```bash
cdk destroy
```

## Running tests

- In a terminal run

```bash
python3 -m unittest discover -v
```

## Notes

To deploy and run this application as a lambda, you will need to give your aws account correct permissions and the lambda stack correct permissions. This was difficult to sort out my first time. I may have given my aws account too many permissions in the end. I only have my root account and a dev account. Giving my own dev account too many permissions is ok with me at this moment. You're situation may be different. Because of this, I won't list out all permissions my dev account has here. I will list some articles that may help you. If you get an error similar to `AccessDeniedException: User: arn:aws:iam:::user/cnc is not authorized to perform: ssm:GetParameter` when running `cdk deploy/synth/destory`, you will need to play around with the permissions your aws account has.

Some articles that may help with permissions are:

- [Grant lambda access to Secrets Manager](https://bobbyhadz.com/blog/aws-grant-lambda-access-to-secrets-manager)
- [User not auth to create stack](https://stackoverflow.com/questions/34237218/user-is-not-authorized-to-perform-cloudformationcreatestack)

## [Finage API documentation](https://finage.co.uk/docs/api/us-stock-historical-end-of-day-data)

## [gitlab stockGuru](https://gitlab.com/kinnander/lambdastockguru/-/tree/main)

## [github stockGuru](https://github.com/m-kinnanderRepos/stockguru)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
