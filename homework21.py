test_dict = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}

print("Test dictionary:", test_dict)

value = input("Enter the value to check: ")

count = 0

for key in test_dict:
    if str(test_dict[key]) == value:
        count += 1

print("Frequency of", value, "is:", count)