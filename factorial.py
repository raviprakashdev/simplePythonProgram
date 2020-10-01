#finding factorial of a number n
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("enter a number n: "))
a= "factorial of" + str(n) +"is: "
print(a,fact(n))
