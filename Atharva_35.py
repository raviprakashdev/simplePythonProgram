# Simple program in python for checking for armstrong number
# Python program to check if the number is an Armstrong number or not

y='y'

while y == 'y':            # while loop
# take input from the user
    x = int(input("Enter a number: "))
    
    sum = 0
    
    temp = x
    while temp > 0:           #loop for checking armstrong number
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if x == sum:
      print(x,"is an Armstrong number")
    else:
      print(x,"is not an Armstrong number")  
      
    y=input("WNamt to continue?(y/n)")          #Condition for multiple run     
  
