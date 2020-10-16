#write a list to file
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        myfile.write("\n".join(color))

content = open('abc.txt')
print(content.read())
