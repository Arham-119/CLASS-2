
# 1. Create a list of odd numbers under the input value

num = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, num) if i % 2 != 0]

print("Odd numbers under", num, ":", odd_numbers)


# 2. Capitalize the first letter of every fruit

fruits = ["apple", "banana", "mango", "orange", "grapes"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Updated fruits:", updated_fruits)
