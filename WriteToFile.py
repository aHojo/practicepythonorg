numbers = [1, 2, 3]

with open("numbers.txt", mode="wt", encoding="UTF-8") as f:
    for x in numbers:
        f.write(f"{x}\n")
