firstList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
secondList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
indexList = range(0,1000)
for i in indexList:
    if i in secondList and i in firstList:
        print(i, "is in both lists") 
            
