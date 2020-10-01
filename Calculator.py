def calc(choice, first_num, second_num):
# Python does not have switch case
# There are other ways to implement this, dictionary mapping for example, but I started off with this
    if(choice=='addition' or choice=='add'):
        return first_num+second_num
    elif (choice=='subtraction' or choice=='subtract'):
        return first_num-second_num
    elif(choice=='multiplication' or choice=='multiply'):
        return first_num*second_num
    elif (choice=='division' or choice=='divide'):
        return first_num/second_num

print("This is the Basic Calculator Program")
start=input("Do you wish to start? Type 1 for YES and 0 for NO: ")
st=int(start)
if(st!=1 and st!=0):
    print("I'm going to take that as a YES")
while (st==1):
    num1=input("Enter the first number: ")
    first_num=int(num1)
    # I could use some thing like
    # Press the corresponing number to perform the operation
    # 1. Addition
    # 2. Subtraction
    # And so on, but I wanted to attempt taking a word input
    choice=input("Addition, subtraction, multiplication or division? ")
    choice=choice.lower()
    num2=input("Enter the second number: ")
    second_num=int(num2)
    answer=calc(first_num, choice, second_num)
    a=int(answer)
    print("The answer is "+str(a))
    continue_=input("Do you want to continue? Press 1 for YES and 0 for NO: ")
    st=int(continue_)
    if(st!=1 and st!=0):
        print("I'm going to take that as a no...")

print("Thank you for trying out the Bacic Calculator Program!")
