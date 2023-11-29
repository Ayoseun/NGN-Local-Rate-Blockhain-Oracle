from brownie import Contract, accounts

def main():
    account = accounts[0]
    contract_address = '0xYourContractAddress'  # Replace with the actual contract address

    # ABI of the contract
    contract_abi = [...]  # Replace with the actual ABI

    # Create a contract object using the ABI
    contract = Contract.from_abi("CurrencyRate", contract_address, contract_abi)

    # Call your contract functions
    update_all_data(contract, "Your all data here", account)
    update_latest_price_data(contract, "Your latest price data here", account)

def update_all_data(contract, data, account):
    tx = contract.updateAllData(data, {'from': account})
    tx.wait(1)  # Wait for the transaction to be mined
    print("All data updated.")

def update_latest_price_data(contract, data, account):
    tx = contract.updateLatestPriceData(data, {'from': account})
    tx.wait(1)  # Wait for the transaction to be mined
    print("Latest price data updated.")

if __name__ == "__main__":
    main()
