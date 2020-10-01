from random import randint
gameplay=['Rock','Paper','scissors']
n=3
Computer=gameplay[randint(0,2)]   
Player=False
YourScore=0
ComputerScore=0
i=0
while i<n:

	while Player==False:

		choice=input('choose any of the three Rock,Paper or scissors\n')
		if choice==Computer:
			YourScore=0
			ComputerScore=0
			print('Computer =',Computer)

			print('woah!,Tie.')
		elif choice=='Rock':

			if Computer=='Paper':
				print('Computer =',Computer)

				print('you lose!',Computer,
				 'covered the',choice)
				ComputerScore=ComputerScore+1
			else:
				print('Computer =',Computer)

				print('woah! you win',choice,'damaged the',Computer)
				YourScore=YourScore+1

		elif choice=='Paper':
			   
			if Computer=='Rock':
				print('Computer =',Computer)

				print('woah! you win',choice, 'covered the' ,Computer)
				YourScore=YourScore+1


			else:
				print('Computer =',Computer)

				print('you lose!,',Computer, 'cut the' ,choice)
				ComputerScore=ComputerScore+1


		elif choice=='scissors':

			if Computer=='Rock':
				print('Computer =',Computer)

				print(' you loose,',Computer, 'damaged the', choice)
				ComputerScore=ComputerScore+1
			else:
				print('Computer =',Computer)
				  
				print('you win!',choice, 'cut the', Computer)
				YourScore=YourScore+1
		elif choice=='Stop':
			break;

							
		else :

			print('enter a valid choice')
		Player=True

					
		
	i=i+1



					
print('YourScore=',YourScore)
print('ComputerScore=',ComputerScore)
if YourScore>ComputerScore:
	print('YOU WIN')
elif YourScore<ComputerScore:

	print('YOU LOOSE')
else:
	print('TIE')
					



				
			
		   




	