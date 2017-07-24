import random
firstList = random.sample(range(30),8)
secondList = random.sample(range(30),10)
indexList = range(0,1000)
print(firstList)
print(secondList)
for i in indexList:
    if i in secondList and i in firstList:
        print(i, "is in both lists") 
