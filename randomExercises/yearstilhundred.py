import datetime

name = input("Please enter your name > ")

age = int(input("How old are you > "))

today = datetime.date.today()
tilHundo = 100 - age
yearHundred = today.year + tilHundo

print("Hello %s, in the year %d, you will be 100 years old.\n\
That's %d years from now!"%(name,yearHundred, tilHundo))

num = int(input("Choose a number of times to display the previous message: "))
i = 0
while i < num:
    print(_)
    i += 1
