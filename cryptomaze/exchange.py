def currency_prices():
    import urllib.request, json
    currencies = {} 
    with urllib.request.urlopen("https://poloniex.com/public?command=returnTicker") as url:
        data = json.loads(url.read().decode())
        currencies['bch'] = data['BTC_BCHABC']['last']
        currencies['eth'] = data['BTC_ETH']['last']
        return currencies

