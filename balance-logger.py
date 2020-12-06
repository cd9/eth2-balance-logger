from prometheus_client import start_http_server, Gauge
from time import sleep
from requests import get

VALIDATOR_INDICES = [1,2,3] #REPLACE THIS WITH YOUR VALIDATOR INDEXES
URL_PREFIX = "http://127.0.0.1:5052/eth/v1/beacon/states/finalized/validators/"
UPDATE_INTERVAL = 15

balance_guage = Gauge('validator_balance', 'Validator balance, in ETH', ['index'])
start_http_server(9010)

while (True):
  for validator_index in VALIDATOR_INDICES:
    balance = get(URL_PREFIX+str(validator_index)).json()["data"]["balance"]
    balance_guage.labels(index=validator_index).set(float(balance)/10**9)
  sleep(UPDATE_INTERVAL)
