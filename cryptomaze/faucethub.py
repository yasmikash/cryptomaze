import requests
from cryptomaze.settings import faucethub_api

def send_bitcoin(amount, address):
    url = 'https://faucethub.io/api/v1/send?api_key='+ str(faucethub_api) +'&currency=BTC&amount='+ str(amount) +'&to='+ str(address)
    r = requests.post(url, data = {'key':'value'})
    data = r.json()
    if data['status'] == 200:
        return True
    else:
        return False

def faucet_balance():
    url = 'https://faucethub.io/api/v1/balance?api_key='+ str(faucethub_api) +'&currency=BTC'
    r = requests.post(url, data = {'key':'value'})
    data = r.json()
    if data['status'] ==  200:
        return data['balance']
    else:
        False
