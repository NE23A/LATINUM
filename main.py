# LATINUM
# NE23A

import requests

# API URLs
coinspot_API_URL = 'https://www.coinspot.com.au/api'
cs_api_latest = 'https://www.coinspot.com.au/pubapi/latest'

# Unpack json payloads
response = requests.get(cs_api_latest)
response_json = response.json
#print(type(response_json))
latestPrices = response_json()
print(latestPrices['prices']['btc'])
