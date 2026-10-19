
import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits

password_characters = lowercase + uppercase + numbers

password = []

password.append(random.choice(lowercase))
password.append(random.choice(uppercase))
password.append(random.choice(numbers))

for i in range(7):
    password.append(random.choice(password_characters))

random.shuffle(password)

password = ''.join(password)

print("Your random password is:", password)
