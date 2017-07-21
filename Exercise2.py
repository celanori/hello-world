import sys #to terminate the program later.
mysteryNumber = int(input("Please enter a whole number: ")) #This is the input of the number by the user.
multipleNumber = mysteryNumber % 4  #Variable for the remainder of the input number divided by 4 to determine multiple of 4.
remainderNumber = mysteryNumber % 2 #Variable for the remainder of the input number divided by 2 to determine even or odd.
if multipleNumber  == 0: #if statment to determine if mutiple of 4.
      print("The input number", mysteryNumber, "is a multiple of 4, and therefore even.")
      sys.exit() #terminate the program
if remainderNumber == 0: #if statment to determine odd or even if not a mutiple of 4.
      print("The input number ", mysteryNumber, " even.")
else:
      print("The input number", mysteryNumber, "odd.") 
