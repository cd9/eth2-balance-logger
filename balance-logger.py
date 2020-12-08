from prometheus_client import start_http_server, Gauge
from time import sleep
from requests import get

VALIDATOR_INDICES = [1,2,3] #REPLACE THIS WITH YOUR VALIDATOR INDEXES
URL_PREFIX = "http://127.0.0.1:5052/eth/v1/beacon/states/finalized/validators/"
UPDATE_INTERVAL = 15

balance_gauge = Gauge('validator_balance', 'Validator balance, in ETH', ['index', 'status'])
start_http_server(9010)

while (True):
  for validator_index in VALIDATOR_INDICES:
    response = get(URL_PREFIX+str(validator_index))
    if not response.ok:
      balance_gauge.labels(index=validator_index, status='unknown').set(0)
      continue
    balance = float(response.json()["data"]["balance"])/10**9
    status = response.json()["data"]["status"]
    balance_gauge.labels(index=validator_index, status=status).set(balance)
  sleep(UPDATE_INTERVAL)
