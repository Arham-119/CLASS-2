try:
    age =int(input("Enter the age:"))
    if(age<18):
        raise ValueError
    else:
        print("the age is valid")

except ValueError:
    print("the age is not valid")