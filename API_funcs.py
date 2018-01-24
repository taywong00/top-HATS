import urllib2, json

stock_name = "GOOG"

key = "I47O8J6SBM5S3302"
nkey = "be357bbe74684a12baca0fd3080c112f"

def get_data(stock_name, key):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stock_name + "&interval=1min&apikey=" + stock_name #"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_name + "&interval=1min&apikey=I47O8J6SBM5S3302"
    data = urllib2.urlopen(url)
    #print data.geturl()
    #print data.info()
    d = json.loads(data.read())
    #print d
    return d

def get_exch_rate(from_cur, to_cur):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + from_cur + "&to_currency=" + to_cur + "&apikey=" + key
    data = urllib2.urlopen(url)
    d = json.loads(data.read())
    print d
    return d

def get_news(kind_of):
    url = "https://newsapi.org/v2/top-headlines?country=us&category=" + kind_of + "&apiKey=" + nkey
    data = urllib2.urlopen(url)
    d = json.loads(data.read())
    #print d
    return d

def get_headlines(topic):
    d = get_news(topic)
    #print d
    print json.dumps(d["articles"][0], indent = 4, sort_keys = True)
    print json.dumps(d["articles"][0]["title"], indent = 4, sort_keys = True)
    one = d["articles"][0]["title"]
    two = d["articles"][1]["title"]
    three = d["articles"][2]["title"]
    return [one, two, three]

def get_URLS(topic):
    d = get_news(topic)
    one = d["articles"][0]["url"]
    two = d["articles"][1]["url"]
    three = d["articles"][2]["url"]
    return [one, two, three]
#get_data(stock_name, key)
#get_exch_rate("BTC", "USD")#
#get_news("finance")
