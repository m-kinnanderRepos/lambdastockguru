# import aws_cdk.core as core
# import aws_cdk.assertions as assertions
# from lambda_stock_guru.lambda_stock_guru_stack import LambdaStockGuruStack


# def test_sqs_queue_created():
#     app = core.App()
#     stack = LambdaStockGuruStack(app, "lambda-stock-guru")
#     template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })


# def test_sns_topic_created():
#     app = core.App()
#     stack = LambdaStockGuruStack(app, "lambda-stock-guru")
#     template = assertions.Template.from_stack(stack)

#     template.resource_count_is("AWS::SNS::Topic", 1)


import unittest


class TestStock(unittest.TestCase):

    def test_stock_init(self):
        self.assertTrue("1.23" == "1.23")

if __name__ == '__main__':
    unittest.main()