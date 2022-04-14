#!/usr/bin/env python3

import aws_cdk as cdk

from lambda_stock_guru.lambda_stock_guru_stack import LambdaStockGuruStack


app = cdk.App()
LambdaStockGuruStack(app, "lambda-stock-guru")

app.synth()
