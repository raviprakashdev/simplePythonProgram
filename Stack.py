stack=[]
try:
while True:
	op = int(input("1 push 2 pop 3 display 4 exit"))
	if op==1:
		ele = int(input("enter elem to push "))
		stack.append(ele)
	elif op==2:
		if len(stack) ==0:
			print("empty hai stack ")
		else:
			ele=stack.pop()
			print("popped elements ")
	elif op==3:
		print(stack)
	elif op==4:
		break
	else:
		print("invalid option")
