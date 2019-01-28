from cryptomaze.settings import coinbase_api, coinbase_api_secr
from coinbase.wallet.client import Client
client = Client(coinbase_api, coinbase_api_secr)

account = client.get_primary_account()

def send_bitcoin(address, amount):
    try:
        account.send_money(to=address, amount=amount, currency='BTC')
        return True
    except:
        return False
