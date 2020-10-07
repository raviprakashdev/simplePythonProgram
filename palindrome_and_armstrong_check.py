def palindrome(inp):
    if inp==inp[::-1]:    #reverse the string and check
        print("Yes, {} is palindrome ".format(inp))
    else:
        print("No, {} is not palindrome ".format(inp))


def armstrong(number):
    num=number
    length=len(str(num))
    total=0
    while num>0:
        temp=num%10
        total=total+(temp**length)  #powering each digit with length of number and adding 
        num=num//10
    if total==number:
        print("{} is Armstrong number".format(number) )
    else:
        print("{} is not an Armstrong number".format(number) )

palindrome('qwerewq')
armstrong(407)
