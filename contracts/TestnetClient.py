import os
from dotenv import load_dotenv

from algosdk import account
from algosdk.v2client.algod import AlgodClient

load_dotenv()

SECRET_KEY = os.getenv("API_KEY")

private_key, public_address = account.generate_account()

algod_addr   = 'https://testnet-algorand.api.purestake.io/ps2'

#algod_addr   = 'https://betanet-algorand.api.purestake.io/ps2'

#algod_addr   = 'https://mainnet-algorand.api.purestake.io/ps2'

algod_header = {
    'User-Agent': 'Minimal-PyTeal-SDK-Demo/0.1',
    'X-API-Key': SECRET_KEY
}

algod_client = AlgodClient(
    SECRET_KEY,
    algod_addr,
    algod_header
)

print(algod_client.status())
