with open("fruits.txt") as f:
    file = f.read()
    for i in file.splitlines():
        print(len(i))
