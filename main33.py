def add(P, Q):
    #this function adds two numbers
    return P + Q
def subtract(P, Q):
    #this function subtracts two numbers
    return P - Q
def multiply(P, Q):
    #this function multiplies two numbers
    return P * Q
def divide(P, Q):
    #this function divides two numbers
    return P / Q

#Now we will take inputs from the user
print ("Please select the operation.")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")

choice = input("Please enter choice(a/b/c/d):")

num_1 = int (input ("please enter the first number:"))
num_2 = int (input ("please enter the second number:"))

if choice == 'a':
    print (num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'b':
    print (num_1, "-", num_2, "=", subtract(num_1, num_2))

elif choice == 'c':
    print (num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == 'd':
    print (num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print ("This is an invalid input")