import urllib2, json

stock_name = "GOOG"



def get_data(stock_name, key):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_name + "&interval=1min&apikey=" + stock_name #"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_name + "&interval=1min&apikey=I47O8J6SBM5S3302"

    data = urllib2.urlopen(url)
    print data.geturl() 
    print data.info()
    d = json.loads(data.read())
    print d

get_data(stock_name, "I47O8J6SBM5S3302")
    