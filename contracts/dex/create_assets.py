from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn, AssetOptInTxn
from algosdk import mnemonic
from algosdk.v2client import algod

#DJ24DOMQY6GWI4NY6CFSQFNWREIQYTN6ABQU7DTIBY5KTGGENF3F2RSMJU
user_mnemonic = "input manage barrel job dizzy raise engine canvas metal novel pudding observe disagree advance rapid angry alert season seek dice system acoustic phone absent butter"
#TQSYJU6BRS4ECUTREW6WAVMRK6MR2XAOC6TKQ46QSDQLVXQJE2O3TT63AU
creator_mnemonic = "woman series evolve retreat alley update afford loop oven royal city bulk false chase arrow guess hood blade room year flower type ivory about daughter"

algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

algod_client = algod.AlgodClient(algod_token, algod_address)


def wait_for_confirmation(client, txid):
    """
    Utility function to wait until the transaction is
    confirmed before proceeding.
    """
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print("Waiting for confirmation")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
    return txinfo


params = algod_client.suggested_params()
params.fee = 1000
params.flat_fee = True

txn = AssetConfigTxn(
    sender=mnemonic.to_public_key(creator_mnemonic),
    sp=params,
    total=1000,
    default_frozen=False,
    unit_name="LATINUM",
    asset_name="latinum",
    manager=mnemonic.to_public_key(creator_mnemonic),
    reserve=mnemonic.to_public_key(creator_mnemonic),
    freeze=mnemonic.to_public_key(creator_mnemonic),
    clawback=mnemonic.to_public_key(creator_mnemonic),
    #url="https://path/to/my/asset/details", 
    decimals=0)
# Sign with secret key of creator
stxn = txn.sign(mnemonic.to_private_key(creator_mnemonic))



txid_1 = algod_client.send_transaction(stxn)
print(txid_1)

wait_for_confirmation(algod_client,txid_1)


ptx = algod_client.pending_transaction_info(txid_1)
asset_id = ptx["asset-index"]
print(asset_id)

#optin
txn = AssetOptInTxn(sender = mnemonic.to_public_key(user_mnemonic), sp = params, index = asset_id, note=None, lease=None, rekey_to=None)
stxn = txn.sign(mnemonic.to_private_key(user_mnemonic))
txid_2 = algod_client.send_transaction(stxn)
print(txid_2)

wait_for_confirmation(algod_client,txid_2)


txn = AssetTransferTxn(sender = mnemonic.to_public_key(creator_mnemonic), sp=params, receiver = mnemonic.to_public_key(user_mnemonic), amt =10, index = asset_id, close_assets_to=None, revocation_target=None, note=None, lease=None, rekey_to=None)

stxn = txn.sign(mnemonic.to_private_key(creator_mnemonic))
txid_3 = algod_client.send_transaction(stxn)
print(txid_3)

wait_for_confirmation(algod_client,txid_3)

print( algod_client.account_info(mnemonic.to_public_key(user_mnemonic))['assets'])
print(50 * '----')
print( algod_client.account_info(mnemonic.to_public_key(creator_mnemonic))['assets'])