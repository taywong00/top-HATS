# Team top_HATS
# Holden Higgins, Adam Abbas, Taylor Wong, Samantha Ngo
# SoftDev1 pd7
# P#02 -- This Is the End

import urllib2, json

File = open("av_key.txt", "r")
key = File.read()
print "KEY:" + key
File.close()

File = open("news_key.txt", "r")
nkey = File.read()
print "NKEY:" + nkey
File.close()

def get_data(stock_name):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stock_name + "&interval=1min&apikey=" + key #"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_name + "&interval=1min&apikey="
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
    #print d
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
    #print json.dumps(d["articles"][0], indent = 4, sort_keys = True)
    #print json.dumps(d["articles"][0]["title"], indent = 4, sort_keys = True)
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
