i = 0
mainList  = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
newListUnderFive = [];
newListOverFive = [];
while i < 11:
  if mainList[i] < 5:
      newListUnderFive += [mainList[i]]
      i+=1
  else:
      newListOverFive += [mainList[i]]
      i+=1
print(newListUnderFive)
print(newListOverFive)
