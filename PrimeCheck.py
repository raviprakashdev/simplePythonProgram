# This program will check whether an inputted natural number is a prime number or not.

user_number = 2

# Queries user to enter a number
user_number = int(input("Please enter a natural number: "))

# Check whether the entered prime number is greater than 1
if user_number > 1 :
    # check for factors
    for x in range(2, user_number):
        if (user_number % x) == 0:
            print(user_number, "is not a prime number")
            print(x, "is a factor of", user_number)
            break
    else:
        print(user_number, "is a prime number!")

# if entered number is less than or equal to 1, it is not prime
else:
    print(user_number, "is not a prime number")