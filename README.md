# Black-Market-Scraping-API
This API is written is python and uses Flask to scrape the internet for blackmarket naira price
# Black Market Scraping API
Welcome to the Black Market Scraping API, a Flask-based web application that scrapes black market exchange rates from a website and returns the data as JSON. This API is designed to be simple and easy to use, making it ideal for developers who need real-time access to black market exchange rates.

### Installation
To install the necessary dependencies for this application, run the following command:

create a virtual environment
```
python3 -m venv [your environment name]
```

##### activate the environment
On Mac (Command Prompt):
```
source myenv/bin/activate
```

On Linux (Command Prompt):
```
myenv\Scripts\activate.bat
```

On Windows (PowerShell):
```
myenv\Scripts\Activate.ps1
```

```
pip install -r requirements.txt
```


### Usage:

```
const Web3 = require('web3');

// Initialize Web3 connection
const web3 = new Web3('<YOUR_INFURA_OR_ALCHEMY_URL>');

// Contract ABI
const contractABI = [/* ... Your Contract ABI ... */];

// Contract Address
const contractAddress = '<YOUR_CONTRACT_ADDRESS>';

// Create contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Event listener
contract.events.RateUpdated({
    fromBlock: 0
}, function(error, event) {
    if (error) {
        console.error(error);
    } else {
        console.log('Rate Updated Event:', event.returnValues);
    }
}).on('data', function(event){
    console.log('New Rate:', event.returnValues); 
    // Here you can process the rate data
});
```


- Running the Script
Run this script in your Node.js environment. It will listen for the RateUpdated events emitted by your smart contract and log the data to the console. You can modify this script to process the data as needed, such as storing it in a database or displaying it in a user interface.

- Processing the Data
When the event is detected, your script will receive the data. You can then process or store this data in any way that suits your application.

- Important Considerations
Historical Data: If you need historical data, your script must query past blocks. The fromBlock parameter in the event listener can be set to the block number from which you wish to start listening.
Real-Time Updates: For real-time data, your script should continuously run and listen for new events.
Network Selection: Ensure your script is pointed at the correct Ethereum network (Mainnet, Testnet, etc.) where your contract is deployed.
Using events for data retrieval is efficient and cost-effective, especially for applications that do not require on-chain interaction for every data retrieval operation.

## Whys is the data only emitted and not saved in the contract state varaible

The difference between saving data in a smart contract's variable and only emitting it via an event lies in several key aspects of blockchain operation and data management.

 Let's break down these differences:

1. Storage Location and Accessibility
Saving in a Variable: When you save data in a contract's state variable, it becomes part of the blockchain's permanent state. This means the data is stored on every node in the network and can be accessed directly by any function within the contract or by external contracts. However, every state change (like updating or adding a new entry) requires a transaction, which costs gas.

Emitting as an Event: Emitting data via an event logs the information in the blockchain's transaction logs but not in its permanent state. This data is not directly accessible by the smart contract's functions after it's emitted. It's mainly used for off-chain access. Listening and reacting to these events is a common practice in DApp (Decentralized Application) development. Events are much cheaper in terms of gas costs compared to storing data.

2. Gas Costs and Efficiency
Saving in a Variable: This is more gas-intensive, especially if the stored data is large or updated frequently. The larger the data, the more gas it costs to perform transactions that update this data.

Emitting as an Event: Emitting events is significantly less expensive in terms of gas costs. It's a cost-effective way to record information that doesn't need to be stored in the contract's state.

3. Use Cases and Application
Saving in a Variable: Ideal for data that needs to be read and manipulated by the contract itself, like updating balances, managing states of a process, or when other contracts need to access this data.

Emitting as an Event: Suitable for logging information for external use, like notifying a user interface of a transaction's outcome, tracking historical transactions, or for any case where the data does not need to be directly accessed by the smart contract after it's been logged.

4. Data Persistence and Blockchain Load
Saving in a Variable: Creates more data that must be stored by every node in the blockchain, contributing to the blockchain's size and the load on each node.

For a real time data analytics emitting as an Event reduces the load on the blockchain because the data is not stored in the blockchain's state. It's ideal for reducing blockchain bloat, particularly for data that is only relevant off-chain.