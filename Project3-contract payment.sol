pragma solidity >=0.4.24 <0.6.0;

contract PaymentChannel{
    address payable public buyer;      // the account sending payments
    address payable public seller;   // the account receiving the payments
    uint256 public expiration;          // timeout in case the seller never closes the channel
    
  
    // in the constructor pass in the seller address and the duration of the payment channel
    constructor (address payable _recipient, uint256 duration) public payable {
        buyer = msg.sender;
        seller = _recipient;
        expiration = now + duration;
    }


    // the seller can close the channel at any time 
    // and the remainder will go back to the buyer
    function close(uint256 amount) public {
        require(msg.sender == seller);
        seller.transfer(amount);
        selfdestruct(buyer);
    }


    // the buyer can extend the expiration of the contract at any time
    function extend(uint256 newExpiration) public {
        require(msg.sender == buyer);
        require(newExpiration > expiration);
        expiration = newExpiration;
    }

    // if the timeout is reached without the seller closing the channel,
    // then the Ether is released back to the buyer.
    function claimTimeout() public {
        require(now >= expiration);
        selfdestruct(buyer);
    }
}
