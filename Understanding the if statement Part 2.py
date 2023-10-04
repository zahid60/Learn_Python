'''var1 = 4
var2 = 5
var3 = 5
if var1 != var2 == var3:
    print("Yes")
else:
    print("No")'''

person1_name = input("What is your Name: ")
person1_wallet = input("How much money do you have: ")

person2_name = input("What is your Name: ")
person2_wallet = input("How much money do you have: ")

person3_name = input("What is your Name: ")
person3_wallet = input("How much money do you have: ")

if float(person1_wallet) > float(person2_wallet) and float(person1_wallet) > float(person3_wallet):
    print(person1_name + " is the richest")
if float(person2_wallet) > float(person1_wallet) and float(person2_wallet) > float(person3_wallet):
    print(person2_name + " is the richest")
if float(person3_wallet) > float(person1_wallet) and float(person3_wallet) > float(person2_wallet):
    print(person3_name + " is the richest")
