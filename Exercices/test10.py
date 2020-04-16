phone = input("Phone: ")
numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}
result = ""
for num in phone:
    result += numbers.get(int(num), "Zero") + " "
print(result)