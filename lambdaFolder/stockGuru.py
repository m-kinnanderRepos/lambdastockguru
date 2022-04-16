import json
from getSecret import get_secret
from stocks import *
from api_classes import *
from stock_classes import Stock, Advice
# Used for testing locally
# ------------------------
# import os
# import sys
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from lambdaFolder.getSecret import get_secret
# from lambdaFolder.stocks import *
# from lambdaFolder.api_classes import *
# from lambdaFolder.stock_classes import Stock, Advice
# ------------------------



def handler(event, context):
    configFile: HistoryApiConfig = HistoryApiConfig(get_secret())
    listOfStocks = []
    # TODO: Have stock name and price be a key/value in secrets manager.
    listOfStocks.append(Stock("AMC", 10.00))
    
    data = get_data(listOfStocks, configFile)
    if(data == 0):
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'Error in call to Stock api'
        }
    
    decisionMakingAdvice = stockDecisionMaking(data)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': '{}'.format(decisionMakingAdvice[0].decision())
    }


if __name__ == "__main__":
    configFile: HistoryApiConfig = HistoryApiConfig(get_secret())
    listOfStocks = []
    listOfStocks.append(Stock("AMC", 10.00))
    
    data = get_data(listOfStocks, configFile)
    if(data == 0):
        print('Error with api call')
    else:
        decisionMakingAdvice = stockDecisionMaking(data)
        print(decisionMakingAdvice[0].decision())
    