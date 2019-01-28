from coinbase.wallet.client import Client
client = Client('e30pkf3soRftrKWy', '8X5CdREU7N7I2snikY0Tq9UGBwT3URoL')

account = client.get_primary_account()

def send_bitcoin(address, amount):
    try:
        account.send_money(to=address, amount=amount, currency='BTC')
        return True
    except:
        return False