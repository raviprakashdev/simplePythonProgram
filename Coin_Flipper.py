import random

def flip():
	n = random.randint(0,1)
	if n == 1:
		return True
	else:
		return False

def user_prompt():
    while True:
        try:
            userInput = input("Please enter a number of flips: ")
            userInput = int(userInput)
            if num_validity(userInput):
                break
            else:
                print("Please Enter a valid Number which is more than 0")
        except ValueError:
            print("Please Enter a valid Number")
        
    return userInput

def num_validity(flips):
    return flips > 0

def main(num):
	heads_count = 0
	tails_count = 0
	result= ""

	for i in range(int(num)):
		if (flip()):
			heads_count+=1
			result += "H "
		else:
			tails_count+=1
			result += "T "
	
	print("Number of Heads: %i" % (heads_count))
	print("Number of Tails: %i" % (tails_count))
	print(result)

Input = user_prompt()
main(Input)