# Floyd-alogrithm
This is a python script of the floyd algorithm which is represented as a class.
The class take in variables known as vertices(expressed in integers which must be more than one)

Another variable would be edges expressed in a list of tuples containing elements that are integers
between 0 and the number of vertices e.g. 0<=x<5.

Another varible would be values ,which is the value correponding to each of the edge in edges respectively, where it is expressed as a list where each element is expressed in terms of float.

The final variable would directed which is tell where an edge has a certain direction or not such as (2,1) means the edge has direction from vertex 1 to 0. This would be expressed as a list of values that can either 0 or 1. If it is 0 its not directed. If its 1 it has direction

The class has also methods:

activate(): simply activates the floyd algorithm however this won't be displayed but rather used within other methods.

distancematrix():This prints the distance matrix after algorithm has been applied.

routematrix():This prints out the routematrix after algorithm has been applied.

distancelength(), parameters-vertexs: This gives the length between two vertices. Must be expressed as tuple containing two elements e.g.(1,2) if vertices => 3

routelength() parameters-vertexs: This gives the route between two vertices. Must be expressed as tuple containing two elements e.g.(1,2) if vertices => 3 
  



























