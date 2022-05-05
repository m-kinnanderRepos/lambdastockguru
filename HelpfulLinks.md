# Sites that helped me build lambdaStockGuru

lambdaStockGuru is a program to help monitor your stocks. These are sites I found helfpul when I created this project. I hope you too find them helpful or learn something new from one of them.

### In no particular order.

## [Working with AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/work-with.html#work-with-prerequisites)

## [Working with AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)

## [aws lambda readme docs](https://docs.aws.amazon.com/cdk/api/v1/docs/aws-lambda-readme.html)

## [Hello Lambda Project](https://cdkworkshop.com/30-python/30-hello-cdk/200-lambda.html)

I first followed this project to create my first lambda. I wanted something simple so I could make sure the deployment was working and I could get a lambda working in aws. This article was much appreciated. After getting this intial project working, adding the stockGuru code was simple.

## [Youtube tutorial going through Hello Lambda Project](https://www.youtube.com/watch?v=-iO4r7rNims)

I ran into an issue with folder structure in the begining. This tutorial really helped clarify what I was suppose to do. This tutorial was also much appreciated.

## [How to create IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)

This was the first time I worked with aws from scratch. I've had experiences creating a lambda and deploying via cdk. My aws account and permissions had already been set up for work though.

## [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)

## [Accessing Secrets from lambda](https://aws.amazon.com/blogs/networking-and-content-delivery/securing-and-accessing-secrets-from-lambdaedge-using-aws-secrets-manager/)

Really good begining to end tutorial for creating a new Secret to accessing it through code. (After creating a Secret, there is sample code at the bottom after opening an individual Secret.)

## [Provision lambda and lambda layers](https://dev.to/upupkenchoong/how-to-provision-lambda-and-lambda-layer-with-cdk-2ff4)

## [Grant lambda access to secrets](https://bobbyhadz.com/blog/aws-grant-lambda-access-to-secrets-manager)

## [Add permissions to lambda function in cdk](https://bobbyhadz.com/blog/aws-cdk-add-lambda-permission)

Your lambda will need permission when requesting Secret values. This tutorial taught me how to create a policy and attach policy to function through code.

## [More info about cdk bootstrap](https://docs.aws.amazon.com/cdk/v2/guide/cli.html#cli-bootstrap)

## [Getting started with AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

If you have not developed with aws cdk before, this guide is a must.

Early mistake I made: I made the mistake when following this guide of using the wrong region when running `aws config`. This lead to issue with running `cdk bootstrap` and `cdk deploy`. I was seeing errors about `Bucket named 'bucket-name' exists, but not in account [object Object]. Wrong account?`. This was extremely hard to debug. I wasn't able to understand what happened until I noticed default region while in aws console was us-east-1 and the region I used in config was us-west-2. This created unexpected errors with bucket permissions as a bucket for cdk is made when running `cdk deploy`. After running `aws config` again and specifying the correct region, `cdk deploy` worked just fine for me.
