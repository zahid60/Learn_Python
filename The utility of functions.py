def love(name):
    print("I love " + name)


love("pizza")


# Function Practice
def person1(name):
    print(name + ": Hello, How can i help you?")


def person2_1(food, drink, dessert, name):
    name = input("What is your name: ")
    drink = input("What do you want to drink: ")
    food = input("What  do you want eat: ")
    dessert = input("What dessert do you want: ")
    print(name + ": I would like " + food + " I want drink " + drink + " I want " + dessert + " as a dessert.")


def person1_2(name):
    print(name + ": Thank you.")


person1("Cashier")
person2_1("food", "drink", "dessert", "name")
person1_2("Cashier")
