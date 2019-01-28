faucet_name = "Cryptomaze" # Your faucet name
faucet_url = "https://cryptomaze.win/" # Your faucet site address url should be included with the trailing slash
time = 300  # Time for each cliam in seconds
sending_time = 86400  # should be in seconds
claim = {'starting amount': 0.00000005, 'last amount': 0.00000050}
threshold = 0.00000001
discount_list = {
    (1, 100): 5,
    (100, 500): 15,
    (500, 1000): 35,
    (1000, 10000): 50
}
sorted_discount_list = sorted(discount_list.items(), key=lambda kv: kv[1])

max_commission = 70 # Max commission as persentage

# include your re-captcha public and private keys
pri_key = "6LeEdHsUAAAAAEP676Av5roxNRcFc1kYs4USVjvU" # private key
pub_key = "6LeEdHsUAAAAANH-6_C46-6yTPaMQiy96rk611wy" # public key
