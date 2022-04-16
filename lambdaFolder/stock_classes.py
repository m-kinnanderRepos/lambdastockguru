from api_classes import HistoryApiConfig, HistoryResponse
# Used for testing locally
# ------------------------
# import os
# import sys
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from lambdaFolder.api_classes import HistoryApiConfig, HistoryResponse
# ------------------------



class Stock:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Advice:
  def __init__(self, historyResponse: HistoryResponse, stock: Stock, averageFiveDaysAgo, diff, finalDecision):
    self.historyResponse = historyResponse
    self.stock = stock
    self.averageFiveDaysAgo = averageFiveDaysAgo
    self.diff = diff
    self.finalDecision = finalDecision

  def decision(self):
      return (f"For {self.stock.name}. "
      f"Buying price was: {self.stock.price}. "
      f"High for 5 days ago is : {str(self.historyResponse.high)}. "
      f"Low for 5 days ago is : {str(self.historyResponse.low)}. "
      f"Average of the two is : {str(self.averageFiveDaysAgo)}. "
      f"Diff is : {str(self.diff)}. "
      f"{self.finalDecision}. ")