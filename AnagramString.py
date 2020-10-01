#a word, phrase, or name formed by rearranging the letters of another
#example silent and listen
#a good additionalitt to this program would be to check whether they are actuallly words or not :)

def mysort(s):    	#function that splits the letters
	d=sorted(s)
	s=''.join(d)
	return s

s1=input("enter first string")
n1=mysort(s1) #function invocation /calling the function

s2=input("enter second string")
n2=mysort(s2)

if n1==n2:
	print("anagram")
else:
	print("not an anangram")