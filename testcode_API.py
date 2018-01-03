import urllib2, json

stock_name = "GOOG"

key = "I47O8J6SBM5S3302"

def get_data(stock_name, key):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_name + "&interval=1min&apikey=" + stock_name #"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_name + "&interval=1min&apikey=I47O8J6SBM5S3302"

    data = urllib2.urlopen(url)
    #print data.geturl()
    #print data.info()
    d = json.loads(data.read())
    print d
    return d

def get_exch_rate(from_cur, to_cur):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + from_cur + "&to_currency=" + to_cur + "&apikey=" + key
    data = urllib2.urlopen(url)
    d = json.loads(data.read())
    print d
    return d

#get_data(stock_name, key)

get_exch_rate("BTC", "USD")
    
