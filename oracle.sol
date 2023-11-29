// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CurrencyRate {
    // Event declarations
    event AllDataUpdated(string data);
    event LatestPriceUpdated(string latestPrice);

    // Function to emit event with the full data array
    function updateAllData(string memory _data) public {
        emit AllDataUpdated(_data);
    }

    // Function to emit event with the latest price data
    function updateLatestPriceData(string memory _data) public {
        emit LatestPriceUpdated(_data);
    }
}
