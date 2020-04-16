weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = 1
    print(f"you are {weight} Pounds")
else:
    converted = 2
    print(f"you are {weight} Kg")
print(converted)
