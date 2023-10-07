our_password = "pass123"
your_answer = " "
number_of_try = 0
number_of_max_try = 4
max_try = "Not Reached"

while your_answer != our_password and max_try != "Reached":
    if number_of_try < number_of_max_try:
        your_answer = input("What is the password ")
        number_of_try = number_of_try + 1
    else:
        max_try = "Reached"

if max_try == "Reached":
    print("Account Blocked")
else:
    print("Access Granted")
