# Team top-HATS
## Members: 
* Taylor Wong - PM, HTML/CSS/Jinja, App.py work
* Samantha Ngo - Accounts, Leaderboard, App.py work
* Adam Abbas - API Work for News and Transactions
* Holden Higgins - Database work for Accounts and Transactions

# STOK

#### Description:
Welcome to Stok, the stock market simulator that lets you play the stock market game... and more! To begin, create an account and choose your "I am" trait. This will determine your profile picture. After that, you're all set to get trading! We'll give you $100,000 (USD) to start off with. Make a transaction by entering a stock ticker name and the number of shares you'd like to purchase. After that, wait for the market to fluctuate, and decide when to sell your shares, hopefully when you've made a profit. In the meantime, you may head over to our News page, to look at the latest finance news (thanks to the News API). Or, look at the leaderboard, where you can see who's been having a good time on the stock market.


### [Watch our demo here.](https://github.com/taywong00/top-HATS)

#### Running our Project

##### First you're going to want to procure some API KEYS.

###### News API:
The News API provided current, relevant news updates from a varitety of sources that were then used in our feed. 
* Go to the [News API page](https://newsapi.org/account)
* Create an account!
* Get your API Key!!!!
* Paste this key into news\_key.txt file.

###### Alphavantage API:
The AlphaVantage API provided all the informations needed regarding stocks and their real-time data
* Go to the [Alphavantage API page](https://www.alphavantage.co/support/#api-key)
* Create an account!
* Get your API Key!!!!
* Paste this key into av\_key.txt file.


#### Now let's run the Project

* Type in `python app.py` into your terminal
* Open up your web browser and head to `localhost:5000`
* You should be at the homepage! Make an account to get started, or log on to pick up where you left off!

### API Dependencies
* Alphavantage API
* News API

### Installation Dependencies
Must be installed using "pip install" in terminal:
* Flask
* SQLite
* pytz

## OR

###### You can also play without having to download anything by going to http://165.227.85.220 and creating an account
