pragma solidity ^0.5.0;

//import "./SharkTankTransactions.sol";
contract SharkTankAuction {
    address investor; //deployer
    address payable public company; //beneficiary

    // Current state of the auction.
    address public highestInvestor; //highestBidder
    uint public highestInvestment; //highestBid
    uint public investedEquity;

    // Surplus amount in waiting list after equity has fully spent
    mapping(address => uint) investedAmount; //pendingReturns
    mapping (string => uint) companyposition;
    mapping (address => uint) companyaddressposition;

    // Set to true at the end, disallows any change.
    // By default initialized to `false`.
    bool public ended;

    // Events that will be emitted on changes.
    event HighestBidIncreased(address bidder, uint amount);
    event LatestInvestment(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);
    event EquityRemaining(string company, uint amount);
    event WaitingList(uint percent, uint amount);

    // The following is a so-called natspec comment,
    // recognizable by the three slashes.
    // It will be shown when the user is asked to
    // confirm a transaction.
    
    struct Company {
        string name;
        address companyAddress;
        uint EquityRaised;
        uint EquityAmount;
    }
    
    Company[] public companies;
    

    constructor(
        address payable _company
    ) public {
        investor = msg.sender; 
        company = _company;
    }
    
    function addParser() public{
        companies.push(Company("Parser.run", 0x5d2173e4C47ad55F32AfEFE96809EC04d7a5d8D5, 100, 100000000));
    }
    
    
    function addCompany(string memory _name, address payable sender, uint _amount) public {
        uint id = companies.push(Company(_name, sender, 0, _amount)) -1;
        companyposition[_name] = id;
        companyaddressposition[sender] = id;
    }

    /// Invest in company with the value sent
    /// together with this transaction.
    /// The value will only be refunded if there
    /// is not enough available equity.
    function invest(string memory _company, address payable sender) public payable {
        // If there is no longer any equity available, send the
        // money back.
        require(
            msg.value > (companies[companyposition[_company]].EquityAmount-companies[companyposition[_company]].EquityRaised),
            "There is not enough available equity."
        );
        require(!ended, "Company has reached its issuance goal and no longer has any available equity.");

        investedEquity += msg.value;
        companies[companyposition[_company]].EquityRaised += msg.value;
        investedAmount[msg.sender] += msg.value;
        emit LatestInvestment(sender, msg.value);
        emit EquityRemaining(_company, companies[companyposition[_company]].EquityAmount);
    }
    
    //function for investor to enter skills/expertise/network regarding the company

    /// Withdraw an investment that was successful.
    // James issues: Complications if an investor has put money in more than one company
    // function withdraw(string memory _company) public returns (bool) {
    //     uint amount = investedAmount[msg.sender];
    //     if (amount > 0) {
    //         // It is important to set this to zero because the recipient
    //         // can call this function again as part of the receiving call
    //         // before `send` returns.
    //         investedAmount[msg.sender] = 0;

    //         if (!msg.sender.send(amount)) {
    //             // No need to call throw here, just reset the amount owing
    //             investedAmount[msg.sender] = amount;
    //             return false;
    //         }
    //     }
    //     companies[_company].EquityAmount + amount;
    //     return true;
    // }

    function totalInvestedAmount(address sender) public view returns (uint) {
        return investedAmount[sender];
    }

    /// End the auction and send the highest bid
    /// to the beneficiary.
    function marketEnd() public {
        // It is a good guideline to structure functions that interact
        // with other contracts (i.e. they call functions or send Ether)
        // into three phases:
        // 1. checking conditions
        // 2. performing actions (potentially changing conditions)
        // 3. interacting with other contracts
        // If these phases are mixed up, the other contract could call
        // back into the current contract and modify the state or cause
        // effects (ether payout) to be performed multiple times.
        // If functions called internally include interaction with external
        // contracts, they also have to be considered interaction with
        // external contracts.

        // 1. Conditions
        require(!ended, "auctionEnd has already been called.");
        require(msg.sender == company, "You are not the auction deployer!");

        // 2. Effects
        ended = true;
        //emit AuctionEnded(highestBidder, highestBid);

        // 3. Interaction
        company.transfer(companies[companyaddressposition[msg.sender]].EquityRaised);
    }
    
}