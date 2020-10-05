"""
Author: Jay Paliwal
Desc: And implementation of the stack data structure using arrays.
"""

class Stack:

    def __init__(self,size):
        self.stack=[]
        self.size=size
        self.top=-1
    
    def push(self):
        if self.top>=self.size-1:
            print("Stack overflow")
        else:
            val=int(input("Enter the value to be pushed: "))
            self.top+=1
            self.stack.insert(0,val)
    
    def pop(self):
        if self.top<=-1:
            print("Stack underflow")
        else:
            self.top-=1
            print("Popped element: ",self.stack.pop(0))
    
    def peek(self):
        if self.top==-1:
            print("Stack empty")
        else:
            print("Elemet at the top is: ",self.stack[0])
    
    def display(self):
        if self.top==-1:
            print("Stack emppty.")
        else:
            print("The stack elements are: ",*self.stack)

    def empty(self):
        if self. top==-1:
            print("Stack is already empty")
        else:
            print("The elements deleted from the stack are: ",*self.stack)
            self.top=-1     
        

stack_size=int(input("Enter the size of the Stack: "))
stk=Stack(stack_size)
while True:
    fn=input("\nMenu:\n1. Enter 'push' to push new element\n2. Enter 'pop' to pop top element\n3. Enter 'peek' to view top elemnt\n4. Enter 'display' to display all elemts of stack\n5  Enter 'empty' to display current stack elemets and clear the stack\n6. Enter 'exit' to end program\n")
    print("\n")
    if fn=="exit":
        break
    elif fn=="push":
        stk.push()
    elif fn=="pop":
        stk.pop()
    elif fn=="peek":
        stk.peek()
    elif fn=="display":
        stk.display()
    elif fn=="empty":
        stk.empty()
    else:
        print("Enter a valid input")


