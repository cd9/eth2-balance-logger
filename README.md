## Ethereum 2.0 Beacon Node validator balance Prometheus Exporter

Simple Python script to fetch an [Ethereum 2.0 Validator Balances](https://ethereum.github.io/eth2.0-APIs/#/Beacon/getStateValidator) from a local beacon node HTTP server and export them as a Prometheus Gauge metric.

# Suggested Usage

1. `pip3 install prometheus_client`
2. Replace the `VALIDATOR_INDICES` array with the indices of the validators you want to track (you can check beaconscan.com if you don't know your indices).
3. Replace the `UPDATE_INTEVAL` with the desired refresh rate of your metric.
4. Run `python3 /PATH/TO/SCRIPT/balance-logger.py` as a service to keep it running permanently.
5. Add port `http://127.0.0.1:9010` as a prometheus target in your `prometheus.yml`.
6. Metric will appear as `validator_balance` in Grafana. 

# Notes

- You should probably wait for your ETH2 beacon-node HTTP server to be up before starting this script, otherwise this script will crash.

- For bonus points, install [CryptoWat](https://docs.prylabs.network/docs/prysm-usage/monitoring/currency-converter/) to convert the balances to local currency.
