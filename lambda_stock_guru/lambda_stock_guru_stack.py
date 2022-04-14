from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam
)


class LambdaStockGuruStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        stockGuru_lambda_layer = _lambda.LayerVersion(
               self, 'StockGuruLambdaLayer',
               code=_lambda.Code.from_asset('package'),
               compatible_runtimes=[_lambda.Runtime.PYTHON_3_7],
               description='Libraries needed from requirements.txt file',
               layer_version_name='v1'
           )

        stockGuru_lambda_policy = iam.PolicyStatement(
                actions=["secretsmanager:GetSecretValue","secretsmanager:DescribeSecret","secretsmanager:ListSecretVersionIds","secretsmanager:PutSecretValue","secretsmanager:UpdateSecret","secretsmanager:TagResource","secretsmanager:UntagResource"],
                resources=["full-arn-path-to-secret"]
        )

        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'StockGuruHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            layers=[stockGuru_lambda_layer],
            code=_lambda.Code.from_asset('lambda'),
            handler='stockGuru.handler',
            initial_policy=[stockGuru_lambda_policy]
        )