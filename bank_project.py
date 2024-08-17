from os import system
from datetime import datetime

system("cls")

class Bank_Account:
     def __init__(self, balance: float, owner_name: str, owner_id: int, owner_phone_number: str, payment_history: list) -> None:
          self.__balance = balance
          self.__owner_name = owner_name
          self.__owner_id = owner_id
          self.__owner_phone_number = owner_phone_number
          self.__payment_history = payment_history

     def get_info(self):
          return f"""
Balans : {self.__balance}
Ism    : {self.__owner_name}
ID     : {self.__owner_id}
Contact: {self.__owner_phone_number}
"""

     def get_owner_name(self):
          return self.__owner_name
     
     def get_owner_id(self):
          return self.__owner_id
     
     def get_owner_balance(self):
          return self.__balance
     
     def get_payment_history(self):
          return self.__payment_history
     
     def set_name(self, new_name):
          self.__owner_name = new_name
     
     def set_phone_number(self, new_number):
          self.__owner_phone_number = new_number
     
     def add_balance(self, summa_plus):
          self.__balance += summa_plus
          transfer_history_add = {
               "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
               "account_id" : self.__owner_id,
               "action": "Qabul qilish",
               "amount": summa_plus
          }
          self.__payment_history.append(transfer_history_add)

     
     def withdraw_balance(self, summa_minus):
          if summa_minus <= self.__balance:
               self.__balance -= summa_minus
               transfer_history_min = {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "account_id": self.__owner_id,
                    "action": "o'tkazish",
                    "amount": summa_minus
               }
               self.__payment_history.append(transfer_history_min)
          else:
               print("Mablag' yetarli emas!")

     
     def transfer(self, account, summa_transfer):
          if summa_transfer <= self.__balance:
               self.__balance -= summa_transfer
               account.__balance += summa_transfer
               
               transfer_history = {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "sender_id": self.__owner_id,
                    "receiver_id": account.__owner_id,
                    "amount": summa_transfer
               }
              
               self.__payment_history.append(transfer_history)
               account.__payment_history.append(transfer_history)
               print(f"Transfer {summa_transfer} O'zkazilindi .")
          else:
               print("Mablag' yetarli emas!")


account1 = Bank_Account(100_000, "Ziyodulla", 23201, "90-478-32-05", [])
account2 = Bank_Account(50_000, "Sardor", 24653, "90-564-32-46", [])

print("Boshlang'ich hisob raqamlar :")
print(f"account1: {account1.get_owner_balance()} \naccount2: {account2.get_owner_balance()}")
print("\n")


account1.transfer(account2, 30_000)
print(f"account1  balance: {account1.get_owner_balance()}")
print(f"account2  balance: {account2.get_owner_balance()}")

print("\nTransfer tarixi account1:")
print(account1.get_payment_history())


account2.transfer(account1, 20_000)
print(f"account1  balance: {account1.get_owner_balance()}")
print(f"account2  balance: {account2.get_owner_balance()}")

print("\nTransfer tarixi  account2:")
print(account2.get_payment_history())


adding_summa = 15_000
print(f"\n O'tkazma  {adding_summa} => account1.")
account1.add_balance(adding_summa)
print(f"account1  balance: {account1.get_owner_balance()}")

print("\n")

print("account1 transfer tarixi :")

ls1=account1.get_payment_history()
for j in ls1:
     print(j)

print("account2 ni transfer tarixi :")

ls2=account2.get_payment_history()
for i in ls2:
     print(i)
