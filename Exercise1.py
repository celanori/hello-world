i = 0
namePerson = input("Please enter your name: ") #Variable for name.
birthDay = input("Please enter your age: ") #Variable for age.
messageNumber = input("How many times do you wanna see this message?: ")
yearsLater = int(birthDay) + 100
while i < int(messageNumber):
      print("Your name is ", namePerson, " and in 100 years you will be ", yearsLater," years old. \n")
      i += 1
