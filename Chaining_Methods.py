from User_bank_acct import*

#Mike, Tommy and Alex are waiting to be used - hence the yellow squigly of error!!! (under from in line 1)
Sheila = banker("Shelandria", "shells@microphilia.com")

Sheila.deposit(20).deposit(21).deposit(40).withdrawal(76)
Sheila.xfersMoneyTo(Mike,400)
Sheila.check_balance()