from Bank_accounts import *

# Kavin = BankAccount(2000,"Kavin")
# Shiva = BankAccount(2761,"Shiva")

# Kavin.get_balance()
# Shiva.get_balance()

# Kavin.deposit(500)
# Shiva.deposit(9)

# Shiva.withdraw(70)

# Shiva.transfer(100,Kavin)

Mani = InterstRewardsAcct(1000, "Mani")
Mani.get_balance()
Mani.deposit(200)

Kani = SavingAcct(1000,"Kani")
Kani.get_balance()
Kani.withdraw(100)
Kani.transfer(20,Mani)