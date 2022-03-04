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

def get_data(asset_id, min_round, end_round):

    reference_point = min_round
    stride = 10000
    while True:
        if end_round <= reference_point:
            break
        data = algod_indexer.search_transactions(min_round=reference_point, max_round=reference_point+stride, asset_id=asset_id, min_amount=1, limit=10000)
        
        len_slice = len(data['transactions'])
        
        if len_slice == 10000:
            print('Maximum slice size reached. Missing data.')
            #add iterative function here
            #next_token = ''
            # while next != 'Enter correct last next-token':
            # next_token = data['next-token']
            break
        else:

            file = json.dumps(data['transactions'])

            with open(f'data/json_data_{asset_id}_{reference_point}-{stride}.json', 'w') as outfile:
                outfile.write(file)

        reference_point+=10000


print(algod_indexer.health())

min_round = 11611000
max_round = 16711000
usdc = 31566704
get_data(usdc, min_round, max_round)