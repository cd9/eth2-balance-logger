from sys import argv, exit
from prometheus_client import start_http_server, Gauge
from time import sleep
import requests

if len(argv) != 3:
  exit("Usage: balance-logger.py VALIDATOR_ID UPDATE_INTERVAL")

URL = "http://127.0.0.1:5052/eth/v1/beacon/states/head/validators/" + argv[1]
UPDATE_INTERVAL = int(argv[2])
balance_guage = Gauge('balance', 'Validator balance, in ETH')
start_http_server(9010)

while (True):
  response = requests.get(URL)
  if response.ok:
    balance_guage.set(float(response.json()["data"]["balance"])/10**9)
  sleep(UPDATE_INTERVAL)
