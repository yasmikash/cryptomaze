faucet_name = "Cryptomaze" # your faucet name
faucet_url = "https://cryptomaze.win/" # your faucet site address url should be included with the trailing slash
time = 1  # time for each cliam in seconds
claim = {'starting amount': 5, 'last amount': 50}
threshold = 1 # include the threshold in satoshi
discount_list = {
    (1, 100): 5,
    (100, 500): 15,
    (500, 1000): 35,
    (1000, 10000): 50
}
sorted_discount_list = sorted(discount_list.items(), key=lambda kv: kv[1])

max_commission = 70 # max commission as persentage

# include your re-captcha public and private keys
pri_key = "6LeEdHsUAAAAAEP676Av5roxNRcFc1kYs4USVjvU" # private key
pub_key = "6LeEdHsUAAAAANH-6_C46-6yTPaMQiy96rk611wy" # public key

# include your Faucethub.io api key
faucethub_api = "josicoesiuowwe8iewocoicuw8e79weucou"
