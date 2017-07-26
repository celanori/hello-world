firstWord = input("Please enter a word: ")
secondpartWord = firstWord[::-1]
if firstWord == secondpartWord:
        print("This word is a palindrome.")
else:
        print("This word is NOT a palindrome.")
