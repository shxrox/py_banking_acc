# Bank Account OOP Project

This project demonstrates a simple Object-Oriented Programming (OOP) approach to modeling bank accounts in Python. It includes basic account operations such as deposit, withdrawal, transfer, and specialized account types with additional features.

## Project Structure

```
Bank_accounts.py      # Contains all account class definitions
oop_account.py        # Example usage and test cases
__pycache__/          # Python bytecode cache (auto-generated)
```

## Features

- **BankAccount**: Base class for all accounts. Supports deposit, withdrawal, balance check, and transfer.
- **InterstRewardsAcct**: Inherits from `BankAccount`. Adds a 5% bonus to every deposit.
- **SavingAcct**: Inherits from `InterstRewardsAcct`. Charges a withdrawal fee.
- **Custom Exceptions**: Handles insufficient balance scenarios gracefully.

## How to Use

1. **Clone or Download the Repository**

2. **Run the Example Script**

   Open a terminal in the project directory and run:
   ```sh
   python oop_account.py
   ```

   This will execute the example operations defined in [oop_account.py](oop_account.py).

3. **Modify or Extend**

   - To create your own accounts or test other operations, edit [oop_account.py](oop_account.py).
   - All account logic is implemented in [Bank_accounts.py](Bank_accounts.py).

## Class Overview

### [`BankAccount`](Bank_accounts.py)

- `__init__(inital_amount, acct_name)`
- `get_balance()`
- `deposit(amount)`
- `withdraw(amount)`
- `transfer(amount, account)`

### [`InterstRewardsAcct`](Bank_accounts.py)

- Inherits from `BankAccount`
- Overrides `deposit(amount)` to add a 5% bonus

### [`SavingAcct`](Bank_accounts.py)

- Inherits from `InterstRewardsAcct`
- Adds a withdrawal fee (`self.fee = 5`)
- Overrides `withdraw(amount)` to include the fee

## Example Usage

See [oop_account.py](oop_account.py):

```python
from Bank_accounts import *

Mani = InterstRewardsAcct(1000, "Mani")
Mani.get_balance()
Mani.deposit(200)

Kani = SavingAcct(1000, "Kani")
Kani.get_balance()
Kani.withdraw(100)
Kani.transfer(20, Mani)
```

## Error Handling

If you try to withdraw or transfer more than the available balance, a custom `BalanceException` is raised and handled gracefully with a message.

## Output Example

```
Account Mani created. 
Balance = 1000.00/= LKR.

Balance : 
Account 'Mani' 
Balance = 1000.00/= LKR.

Deposit Complted
Balance : 
Account 'Mani' 
Balance = 1210.00/= LKR.
...
```

## Requirements

- Python 3.x

No external dependencies are required.

