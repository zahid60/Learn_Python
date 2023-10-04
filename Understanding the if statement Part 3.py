def quation():
    rules = input("What need to answer every questions by YES or NO do you understand: ")
    if rules != "yes":
        return print("Try again")
    else:
        print("Next question")
    question1 = input("Are you hungry: ")
    if question1 != "yes":
        return print("Then go for walk")
    else:
        print("Next question")
    question2 = input("Do you wan to eat restaurant: ")
    if question2 != "yes":
        return print("Come eat at my place")
    else:
        print("Next question")
    question3 = input("Do you wan to eat pizza: ")
    if question3 != "yes":
        return print("lets go to eat burger then")
    else:
        print("lets go to eat pizza")
quation()