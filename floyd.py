import numpy as np
import sys

class floyd():
    def __init__(self,vertices,edges,values,directed):
        self.vertices = vertices
        self.edges = edges
        self.values = values
        self.directed = directed
        self.distancetable = np.zeros((self.vertices,self.vertices))
        self.routetable = np.zeros((self.vertices,self.vertices),dtype=np.int8)
        if type(self.vertices) is int and self.vertices > 1:
            pass
        else:
            sys.exit('vertices must be an integer and greater than 1')
        if type(self.edges) is list:
            for i in self.edges:
                if type(i) is tuple and len(i) == 2:
                    continue
                else:
                    sys.exit('Each element of the list must be a tuple and there must be exactly two numbers in each of those vertices.(edges)')
                for j in i:
                    if type(j) is int:
                        continue
                    else:
                        sys.exit('each element within the tuple must be an integer.(edges)')
                (x,y) = i
                if x == y:
                    sys.exit('You cannot have edges that are loops, e.g. (1,1),(2,2) etc.(edges)')
                else:
                    continue
        else:
            sys.exit('The edges must be a list')
        if type(self.values) is list:
            for i in self.values:
                if type(i) is float or type(i) is int:
                    print(i)
                    continue
                else:
                    sys.exit('each element in the list must be a float.(values)')
        else:
            sys.exit('values must be a list')
        if type(self.directed) is list:
            for i in self.directed:
                if i == 1 or i == 0:
                    continue
                else:
                    sys.exit('The element in each of the list must be either 0 or 1(directed)')
                
        else:
            sys.exit('values must be a list')
    
    
    def activate(self):
        self.distancetable = np.zeros((self.vertices,self.vertices))
        self.routetable = np.zeros((self.vertices,self.vertices),dtype=np.int8)
        possibleedges = []

        for i in range(0,self.vertices):
            for j in range(0,self.vertices):
                self.routetable[j,i] = i
                possibleedges.append((i,j))

        for i in self.edges:
            if i in possibleedges:
                ind = self.edges.index(i)
                if self.directed[ind] == 0:
                    (x,y) = i
                    possibleedges.remove((x,y))
                    possibleedges.remove((y,x))
                elif self.directed[ind] == 1:
                    (x,y) = i
                    possibleedges.remove((y,x))
                else:
                    continue
            else:
                continue

        for i in range(0,self.vertices):
            for j in range(0,self.vertices):
                if i == j:
                    self.distancetable[i,j] = float('inf')
                else:
                    continue

        for i in range(0,len(self.edges)):
            (x,y) = self.edges[i]
            if self.directed[i] == 0:
                self.distancetable[x,y] = self.values[i]
                self.distancetable[y,x] = self.values[i]
            elif self.directed[i] == 1:
                self.distancetable[x,y] = self.values[i]
            else:
                continue

        for i in range(0,len(possibleedges)):
            (x,y) = possibleedges[i]
            self.distancetable[x,y] = float('inf')

        for x in range(0,self.vertices):
            for i in range(0,self.vertices):
                for j in range(0,self.vertices):
                    if x == i or x == j:
                        continue
                    elif x == i and x == j:
                        continue
                    else:
                        if self.distancetable[i,x] + self.distancetable[x,j] < self.distancetable[i,j]:
                            if i == j:
                                continue
                            else:
                                a = self.distancetable[i,x] + self.distancetable[x,j]
                                self.distancetable[i,j] = a
                                self.routetable[i,j] = x
                        else:
                            continue
        return (self.distancetable,self.routetable) 
    def distancematrix(self):
        (x,y) = self.activate()
        return x
    def routematrix(self):
        (x,y) = self.activate()
        return y
    def routedirection(self,vertexs):
        (i,j) = self.activate()
        directions = []
        (x,y) = vertexs
        directions.append(str(y))
        while j[x,y] != y:
            y = j[x,y]
            directions.append(str(y))
        directions.append(str(x))
        directions.reverse()
        directions = '-'.join(directions)
        return directions
    def directionlength(self,vertexs):
        (i,j) = self.activate()
        (x,y) = vertexs
        if i[x,y] == float('inf'):
            print('undefined length')
        else:
            print(i[x,y])
    






