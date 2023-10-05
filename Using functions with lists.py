food=["hambuger","burger","pizza","juice","banana","hot dog"]
price=[5,65,66,76]

food.insert(2,"grapes") #grapes added in second index
food.extend(price)      #price list added

print(food.index("pizza"))
print(food)
print(food.count("juice"))
random=food.copy()+price.copy()
print(random)