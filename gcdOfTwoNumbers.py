#program to find greatest common divisor(gcd) of two numbers using recursion

#GCD function
def gcd(num1, num2):
    if num2 != 0:
        return gcd(num2, num1%num2)
    else:
        return num1

#driver code
n1 = int(input("Enter a number "))
n2 = int(input("Enter another number "))
result = gcd(n1,n2)
print("GCD : %d " %(result))

