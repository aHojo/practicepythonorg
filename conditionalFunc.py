def stringLength(stringu):
    if (type(stringu) == int):
        return "Sorry integers do not have any length"
    elif (type(stringu) == float):
        return "Sorry float do not have any length"
    return len(stringu)


print(stringLength(10))
print(stringLength("sladfkjas"))
