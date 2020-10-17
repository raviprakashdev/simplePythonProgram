numlist = list()
# User enters list of integers
while True:
  inp = input('Enter a number, enter done to end: ')
  if inp == 'done':
    break
  value = float(inp)
  numlist.append(value)
# Calculate minimum and maximum numbers
minimum = min(numlist)
maximum = max(numlist)
print('Minimum number:', minimum, 'Maximum number:', maximum)
