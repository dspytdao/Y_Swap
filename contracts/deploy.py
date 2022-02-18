from algosdk import *
from pyteal import *
import dex

import os
from dotenv import load_dotenv

from algosdk import account
from algosdk.v2client.algod import AlgodClient

load_dotenv()

SECRET_KEY = os.getenv("API_KEY")

private_key, public_address = account.generate_account()

algod_addr   = 'https://testnet-algorand.api.purestake.io/ps2'

algod_header = {
    'User-Agent': 'Minimal-PyTeal-SDK-Demo/0.1',
    'X-API-Key': SECRET_KEY
}

algod_client = AlgodClient(
    SECRET_KEY,
    algod_addr,
    algod_header
)


try:
    algod_client.status()
except error.AlgodHTTPError:
    quit(f"algod node connection failure\n Check if the Host and API key are correct")

# compile the pyteal contract
approval_teal = compileTeal(dex.approval(), Mode.Application, version=5)
clearstate_teal = compileTeal(dex.clear(), Mode.Application, version=5)

# convert TEAL to bytecode (gets encoded in base64)
approval_b64 = algod_client.compile(approval_teal)["result"]
clearstate_b64 = algod_client.compile(clearstate_teal)["result"]

# Decode the encoded TEAL
approval_prog = encoding.base64.b64decode(approval_b64)
clearstate_prog = encoding.base64.b64decode(clearstate_b64)

# txn params
sp = algod_client.suggested_params()
sp.flat_fee = True
sp.fee = 2_000

# deploy contract
appTxn = future.transaction.ApplicationCreateTxn(
    pk,
    sp,
    future.transaction.OnComplete.NoOpOC,
    approval_prog,
    clearstate_prog,
    future.transaction.StateSchema(5, 10),
    future.transaction.StateSchema(5, 10),
)

sAppTxn = appTxn.sign(sk)
txid = algod_client.send_transaction(sAppTxn)
future.transaction.wait_for_confirmation(algod_client, txid)
print("\x1b[32mApp deployed successfully\x1b[0m")
print("========================================")
print(f"https://testnet.algoexplorer.io/tx/{txid}")
