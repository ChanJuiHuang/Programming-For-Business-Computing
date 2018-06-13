balance1 = int(input())
balance2 = int(input())
transfer_money = int(input())

if transfer_money > balance1:
    balance2 += balance1
    balance1 = 0
else:
  balance1 -=transfer_money
  balance2 +=transfer_money

print(balance1, balance2)
