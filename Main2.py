#input a word
text = str(input("Enter a string: "))

# Reverse String
# using step value as -1 to iterate in reverse
revtext = text[::-1]
text = revtext

print("Reverse of Given String is:")
print(text)