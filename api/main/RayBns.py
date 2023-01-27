from web3 import Web3
import json
import random
import string
from web3.middleware import geth_poa_middleware

import requests
import base64
import ast

bitgertchain = "https://rpc.icecreamswap.com"
#bitgertchain = "https://serverrpc.com"
#bitgertchain = "https://chainrpc.com"


web3 = Web3(Web3.HTTPProvider(bitgertchain))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract_address = Web3.toChecksumAddress('0x7aDaa1db4FF0a6e55214490C7936719446a4d590') #be sure to use a BSC Address in uppercase format like this 0x9F0818B... 

abi = json.loads('[ { "inputs": [ { "internalType": "string", "name": "_tld", "type": "string" } ], "stateMutability": "payable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "approved", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": false, "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "ApprovalForAll", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "approve", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "", "type": "string" } ], "name": "domains", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "getAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "getApproved", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "getRecord", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "operator", "type": "address" } ], "name": "isApprovedForAll", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "isOwner", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [ { "internalType": "address payable", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "ownerOf", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "price", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "", "type": "string" } ], "name": "records", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" } ], "name": "register", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "string", "name": "record", "type": "string" } ], "name": "setRecord", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "tld", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "tokenURI", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "transferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "withdraw", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]')

contract = web3.eth.contract(address=contract_address, abi=abi)



def GetBnsAddress(name):
    name_address = contract.functions.getAddress(name).call()
    return name_address
    
def GetBnsPrice(name):
    name_price = contract.functions.price(name).call()
    return name_price

def Withdraw():
    transaction = contract.functions.withdraw().buildTransaction({'chainId': 32520, 'gas':210000, 'gasPrice': web3.toWei('21','gwei'), 'nonce': web3.eth.getTransactionCount(Web3.toChecksumAddress("0xC15f78E3CE78f2968418FFcE7dD5a353C9d9BB8B"))})
    #return transaction
    
    sign_txn = web3.eth.account.signTransaction(transaction, private_key="df266258d085975a3735424c3ca421bf635f9368adace9d0295a1d4cbb1c3c5e")
    tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    return tx_hash.hex()
    
def GetDetail():
    details = []
    try:
        for item in range(20):
            metadata = contract.functions.tokenURI(item).call()
            
            stripped_resp = metadata.replace("data:application/json;base64,", "")
            decoded_resp = base64.b64decode(stripped_resp)
            decoded_resp = decoded_resp.decode("UTF-8")
            decoded_resp = ast.literal_eval(decoded_resp)
            
            decoded_image = base64.b64decode(decoded_resp["image"].replace("data:image/svg+xml;base64,", ""))
            detail = {"token_id": item, "name": decoded_resp["name"], "address": GetBnsAddress(decoded_resp["name"][0:-6]), "description": decoded_resp["description"], "image": decoded_image}
    
            details.append(detail)
            
    except:
        pass
    
    return details
    
def GetBnsName(address):
    names = GetDetail()
    results = []
    for item in names:
        if item["address"] == address:
            results.append(item["name"])
        
    return results
    
def Transfer(name, address_from, address_to):
    transaction = contract.functions.transferFrom(address_from, address_to, name).buildTransaction({'chainId': 32520, 'gas':210000, 'gasPrice': web3.toWei('21','gwei'), 'nonce': web3.eth.getTransactionCount(Web3.toChecksumAddress("0x88F0CaB22ebAE397ef058F0375dFe037A1b3d69C"))})
    #return transaction
    
    sign_txn = web3.eth.account.signTransaction(transaction, private_key="43d0fed1c4c37c91ac3d5d92fc30965327a12b7eaa0baab756c7ded08adbc3b3")
    tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    return tx_hash.hex()
    