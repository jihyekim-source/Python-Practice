from bank import bank
''''''
myFirstAccount = bank.BankBook('고객1', '010-2733-0000')
myFirstAccount.deposit(5000)
myFirstAccount.withdraw(3000)
myFirstAccount.withdraw(5000)
myFirstAccount.describe() # 해당 함수에서 print()구현할 것

mySecondAccount = bank.BankBook('고객1', '010-5361-0000')
mySecondAccount.deposit(1000)
print('두 통장의 잔고 합 : ', myFirstAccount + mySecondAccount)




