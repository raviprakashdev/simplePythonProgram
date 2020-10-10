"""
Author: Jay Paliwal
Desc: Implementation fo graph using adjecency matrix and calculation 
        of the length of the shortest path using dijkstra's algorithm
"""

import sys

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[0]*vertices]*vertices
    
    def add_edge(self,v1,v2,wt):
        self.graph[v1][v2]=wt
        self.graph[v2][v1]=wt
    
    def dijkstra(self,src,dest): 
        d=[sys.maxsize]*self.vertices 
        d[src]=0
        shrtst_pth=[False]*self.vertices 
        for _ in range(self.vertices):
            min=sys.maxsize 
            for i in range(self.vertices): 
                if d[i]<min and shrtst_pth[i]==False: 
                    min=d[i] 
                    v1=i  
            shrtst_pth[v1]=True
            for v2 in range(self.vertices): 
                if self.graph[v1][v2]>0 and shrtst_pth[v2]==False and d[v2]>(d[v1]+self.graph[v1][v2]): 
                        d[v2]=d[v1]+self.graph[v1][v2]
        print("The length of the shortest path between ",src," and ",dest," is: ",d[dest]

v=int(input("Enter the number of vertices: "))
g=Graph(v)
c='1'
while True:
    c=input("Enter '1' to add a new edge, enter '0' if you are done adding edges: ")
    if c!='0' or c!='1':
        print("Invalid input")
        continue
    elif c=='0':
        break
    a=int(input("Enter first vertex: "))
    b=int(input("Enter second vertex: "))
    if a>=v or a<0:
        print("Invalid value entered for first vertex")
        continue
    if b>=v or b<0:
        print("Invalid value entered for second vertex")
        continue
    wt=int(input("Enter the weight of the edge: "))
    g.add_edge(a,b,wt)

while True:
    src,dest=map(int,input("Enter the source and destination vertex to calculate the shorthest path (source followed by destination): ").rstrip().split())
    if (src>=0 and src<v) and (dest>=0 and dest<v):
        break
    print("Invalid input.")

g.dijkstra(src,dest)