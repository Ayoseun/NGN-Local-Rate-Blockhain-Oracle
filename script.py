from brownie import Contract, accounts, network
import os
import websocket
import threading
import time
import json

def main():
    private_key = os.getenv('PRIVATE_KEY')
    contract_address = os.getenv('CONTRACT_ADDRESS')
    websocket_url = os.getenv('WEBSOCKET_URL')

    if not private_key or not contract_address or not websocket_url:
        raise EnvironmentError("Environment variables not set correctly")

    account = accounts.add(private_key)

    # Ensure you're connected to the correct network
    # network.connect('mainnet')  # or another network

    contract_abi = [
        {
            "anonymous": False,
            "inputs": [
                {"indexed": False, "internalType": "string", "name": "data", "type": "string"}
            ],
            "name": "AllDataUpdated",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": False, "internalType": "string", "name": "latestPrice", "type": "string"}
            ],
            "name": "LatestPriceUpdated",
            "type": "event"
        },
        {
            "inputs": [
                {"internalType": "string", "name": "_data", "type": "string"}
            ],
            "name": "addData",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {"internalType": "string", "name": "_data", "type": "string"}
            ],
            "name": "latestPriceData",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]

    contract = Contract.from_abi("CurrencyRate", contract_address, contract_abi)

    # Start the WebSocket in a separate thread
    threading.Thread(target=listen_to_websocket, args=(websocket_url, contract, account)).start()

def listen_to_websocket(url, contract, account):
    def on_message(ws, message):
        # Process the message and update data
        try:
            data = json.loads(message)
            data_str = json.dumps(data)  # Convert to string if necessary
            update_contract_data(contract, data_str, account)
        except json.JSONDecodeError:
            print("Error decoding JSON from WebSocket")

    def on_error(ws, error):
        print(error)

    def on_close(ws, close_status_code, close_msg):
        print("### WebSocket closed ###")

    def on_open(ws):
        print("WebSocket connection opened")

    ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()

def update_contract_data(contract, data, account):
    tx = contract.updateAllData(data, {'from': account})
    tx.wait(1)
    print("Contract data updated.")

    # You may want to add a delay here if you only want to update periodically
    time.sleep(300)

if __name__ == "__main__":
    main()
