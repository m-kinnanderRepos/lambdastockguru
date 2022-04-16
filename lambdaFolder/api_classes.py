class HistoryResponse:
  def __init__(self, jsonLoads):
    self.high = jsonLoads["high"]
    self.low = jsonLoads["low"]



class HistoryApiConfig: 
  def __init__(self, configFile):
    self.key = configFile["HISTORY_APIURL_KEY"]
    self.daysAgo = int(configFile["DAYSAGO"])
    self.historyApiUrl = configFile["HISTORY_APIURL"]