from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam
)


class LambdaStockGuruStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a layer for our lambda function to have access to third party software
        stockGuru_lambda_layer = _lambda.LayerVersion(
               self, 'StockGuruLambdaLayer',
               code=_lambda.Code.from_asset('package'),
               compatible_runtimes=[_lambda.Runtime.PYTHON_3_7],
               description='Libraries needed from requirements.txt file',
               layer_version_name='v1'
           )

        # The needed policies for a lambda function to access values of keys from secrets manager
        # Will be added to lambda via `initial_policy`
        stockGuru_lambda_policy = iam.PolicyStatement(
                actions=["secretsmanager:GetSecretValue","secretsmanager:DescribeSecret","secretsmanager:ListSecretVersionIds","secretsmanager:PutSecretValue","secretsmanager:UpdateSecret","secretsmanager:TagResource","secretsmanager:UntagResource"],
                resources=["arn:aws:secretsmanager:us-east-2:428386179621:secret:config-history_api-dWq6iZ"]
        )

        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'StockGuruHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            layers=[stockGuru_lambda_layer],
            code=_lambda.Code.from_asset('lambdaFolder'),
            handler='stockGuru.handler',
            initial_policy=[stockGuru_lambda_policy]
        )