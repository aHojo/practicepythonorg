num = int(input("Please enter a number: "))

if num % 4 == 0:
    print("%d is a multple of 4"%(num))
elif num % 2 == 0:
    print("%d is even!"%(num))
else:
    print("%d is odd"%(num))
