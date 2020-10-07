"""
Author: Jay Paliwal
Desc: And implementation of the Queue data structure using arrays.
"""
class Queue:
    def __init__(self,size):
        self.size=size
        self.q=[]
        self.front=-1
        self.rear=-1
    def enqueue(self):
        if self.rear==(self.size-1):
            print("Queue Full")
        else:
            val=int(input("Enter the value to be enqueued: "))
            self.q.append(val)
            self.rear+=1
            if self.front==-1:
                self.front=0

    def dequeue(self):
        if self.rear<0 or self.rear<self.front:
            print("Queue Empty")
        else:
            if self.rear!=self.front:
                print("The value dequeued was: ",self.q.pop(0))
                self.front+=1
            else:
                print("The value dequeued was: ",self.q.pop(0))
                self.front=-1
                self.rear=-1
    def frontdisp(self):
        if self.front==-1:
            print("Queue Empty")
            return 
        print("The element at the front is: ",self.q[0])
    def reardisp(self):
        if self.front==-1:
            print("Queue Empty")
            return
        print("The element at the rear is: ",self.q[len(self.q)-1])
    def display(self):
        if self.front==-1:
            print("Queue Empty")
            return
        print("The elements in the queue are: ",*self.q)
    def empty(self):
        if self.front==-1:
            print("Queue Empty")
            return
        print("The elements being deleted from the queue are: ",*self.q)
        self.q=[]
        self.rear=-1
        self.front=-1
            


Queue_size=int(input("Enter the size of the Queue: "))
que=Queue(Queue_size)
while True:
    fn=input("\nMenu:\n1. Enter 'enqueue' to add new element\n2. Enter 'dequeue' to delete rear element\n3. Enter 'front' to view front most elemnt\n4. Enter 'rear' to view rear most element\n5. Enter 'display' to display all elemts of queue\n6. Enter 'empty' to display current queue elemets and clear the queue\n7. Enter 'exit' to end program\n")
    print("\n")
    if fn=="exit":
        break
    elif fn=="enqueue":
        que.enqueue()
    elif fn=="dequeue":
        que.dequeue()
    elif fn=="front":
        que.frontdisp()
    elif fn=='rear':
        que.reardisp()
    elif fn=="display":
        que.display()
    elif fn=="empty":
        que.empty()
    else:
        print("Enter a valid input")