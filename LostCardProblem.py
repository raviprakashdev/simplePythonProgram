for _ in range(int(input("Enter the number of testcases: "))):
    print("\n\n\nWelcome, We will find one of your lost card...")
    print("\n1. Series Cards\n2. Random Cards\n3. Exit\n\n")
    ch=4
    a=0
    sum=0
    while(ch!=1 and ch!=2 and ch!=3):
        print("Please, Press 1, 2 or 3... ")
        ch=input()
        try:
            ch=int(ch)
        except:
            pass
    if(ch==3):
        exit()
    else:
        n=int(input("Enter the total number of cards you had: "))
        if(ch==1):
            a=n*(n+1)//2
        else:
            print("Enter all the",n,"cards you had: ")
            for i in range(1,n+1):
                a=a+int(input())
        print("Now, enter",n-1,"cards you have now: ")
        for i in range(n-1):
            sum=sum+int(input())
        print("Lost Card: ",a-sum)
