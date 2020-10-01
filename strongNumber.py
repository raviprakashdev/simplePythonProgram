#A Strong number is a number whose sum of factorials of digits is equal to the same number.
#Example: 145 is a Strong Number (1!+4!+5! = 145)

num = int(input("Enter a number\n"))
temp = num
sum = 0
while(temp > 0):
    d = temp % 10
    f = 1
    while(d > 0):
        f = f * d
        d -= 1
    sum += f
    temp = temp // 10
if sum == num:
    print("%d is a Strong Number" %(num))
else:
    print("%d is NOT a Strong Number" %(num))
