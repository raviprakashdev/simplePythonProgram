nlist = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]                             #making a random list
print('List has the items: ', nlist)                                     #printing the items of the list
searchItem = int(input('Enter a number to search for: '))                #asking for the number to be found among the shown list
found = False                                                        
for i in range(len(nlist)):
    if nlist[i] == searchItem:
        found = True
        print(searchItem, ' was found in the list at index ', i)
        break
if found == False:
    print(searchItem, ' was not found in the list!')
