import os
import json
from dotenv import load_dotenv

from algosdk.v2client.indexer import IndexerClient

load_dotenv()

SECRET_KEY = os.getenv("API_KEY")

algod_header = {
    'User-Agent': 'Minimal-PyTeal-SDK-Demo/0.1',
    'X-API-Key': SECRET_KEY
}

indexer_address = "https://mainnet-algorand.api.purestake.io/idx2"

algod_indexer = IndexerClient(
    SECRET_KEY,
    indexer_address,
    algod_header
)

print(algod_indexer.health())

round = 11611093
usdc = 31566704 

"""
for (i) in range(10):
    next_token = ''

    while next_token!="xx":
        
        nt = algod_indexer.asset_balances(asset, limit=2001,  round_num=round, next_page=next_token)
        if 'next-token' not in nt.keys():
            #print(len(nt['balances']))
            next_token ='xx'
            
        else:
            print(len(nt['balances']))
            file = json.dumps(nt)
            #with open(f'json_data_{next_token}_{block}.json', 'w') as outfile:
            ##    outfile.write(file)
            next_token = nt['next-token']
    round += 10000000
"""

data = algod_indexer.search_transactions(min_round=round, max_round=round+10000, asset_id=usdc)['transactions']

file = json.dumps(data)
with open(f'json_data.json', 'w') as outfile:
    outfile.write(file)

print(len(data))