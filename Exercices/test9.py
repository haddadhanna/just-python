numbers = [1, 2, 4, 7, 8, 4, 1, 2, 4, 4, 9]
for item in numbers:
    if(numbers.count(item) > 1):
        numbers.remove(item)
print(numbers)