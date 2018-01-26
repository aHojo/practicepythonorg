someString = str(input("Please enter a string to see if string = palindrome: "))

if someString == someString[::-1]:
    print("String Forward: %s"%(someString))
    print("String Backward: %s"%(someString[::-1]))
    print("This is a palindrome!")
else:
    print("{} is not a palindrome.".format(someString))
    print("String Forward: %s"%(someString))
    print("String Backward: %s"%(someString[::-1]))
