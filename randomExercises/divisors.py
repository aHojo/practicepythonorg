num = int(input("Please enter a number you would like a divisor for: "))

for i in range(2, num + 1):
	if num % i == 0:
		print("Divisors are: %d"%(i))

		