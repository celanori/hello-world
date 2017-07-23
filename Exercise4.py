mysteryNumber = int(input("Please input a number: ")) #The mystery number is the variable for the input. This also helps create our range.
indexList = range(2,mysteryNumber) #This is the range, so we can create the number line of possible numbers to divide the mysteryNumber.
for i in indexList: #This creates an individual number to compare inside the list that we created.
    if mysteryNumber % i == 0: #This checks if the remainder of the specific number evenly divides into the mystery number
        print("The number", i, "does divide evenly into", mysteryNumber) # printed solution for each of the numbers that evenly divide.
