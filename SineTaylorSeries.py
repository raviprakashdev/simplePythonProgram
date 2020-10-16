def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
def sin(x,n):
    power=1
    sign=1
    s=0
    for i in range(n):
        s=s+(sign*(x**power)/fact(power))
        power=power+2
        sign=sign*-1
    return s
print("This program will calculate value of sinx using taylor series upto n terms: ")
x=float(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
print("Calculating...")
print("Value of sinx upto n-terms using taylor series is: ",sin(x,n))
