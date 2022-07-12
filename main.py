import copy
import time
import random

class Vertex:
    def __eq__(self, other):
        pass
    def __hash__(self):
        pass

class Graph:
    def __init__(self, n):
        self.vertices = dict()
        for i in range(n):
            self.vertices[i] = (set(),set())
        self.edges=dict()

    def add_edge(self, x, y,c):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        if y not in self.parse_vertices():
            print("Invalid input!")
            return
        if c==0:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y)  in self.edges:
            print("Edge already there!")
            return
        self.vertices[x][0].add(y)
        self.vertices[y][1].add(x)
        self.edges[str(x)+"-"+str(y)]=c
    def remove_edge(self,x,y):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        if y not in self.parse_vertices():
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges:
            print("Invalid input!")
            return
        self.vertices[x][0].remove(y)
        self.vertices[y][1].remove(x)
        self.edges[str(x) + "-" + str(y)] = 0
    def add_vertex(self):
        self.vertices[self.get_nr_of_vertices()+1]=(set(),set())
    def delete_vertex(self,x):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        new_dic=dict()
        l=self.parse_vertices()
        for i in l:
            if x in self.vertices[i][0]:
                self.vertices[i][0].remove(x)
            if x in self.vertices[i][1]:
                self.vertices[i][1].remove(x)
        del self.vertices[x]
        for key in self.edges:
            if int(key[0])==int(x) or int(key[2])==int(x):
                pass
            else:
                new_dic[key]=self.edges[key]
        self.edges=copy.deepcopy(new_dic)
    def is_edge(self, x, y):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        if y not in self.parse_vertices():
            print("Invalid input!")
            return
        if (y in self.vertices[x][0]):
            return 1, self.edges[str(x)+"-"+str(y)]
        else:
            return 0,0

    def get_cost(self,x,y):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        if y not in self.parse_vertices():
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges:
            print("Invalid input!")
            return
        return self.edges[str(x)+"-"+str(y)]

    def set_cost(self,x,y, new):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        if y not in self.parse_vertices():
            print("Invalid input!")
            return
        if new ==0:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges:
            print("Invalid input!")
            return
        self.edges[str(x)+"-"+str(y)] = new
    def parse_vertices(self):
        vertices_list = list()
        for key in self.vertices:
            vertices_list.append(key)
        return vertices_list

    def parse_nout(self, x):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        nout_vertices = list()
        for y in self.vertices[x][0]:
            nout_vertices.append(y)
        return nout_vertices

    def parse_nin(self, x):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return
        nin_vertices = list()
        for y in self.vertices[x][1]:
            nin_vertices.append(y)
        return nin_vertices
    def get_nr_of_vertices(self):
        return len(self.vertices)
    def get_nr_of_edges(self):
        return len(self.edges)
    def get_out_degree(self,x):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return

        return len(self.vertices[x][0])

    def get_in_degree(self,x):
        if x not in self.parse_vertices():
            print("Invalid input!")
            return

        return len(self.vertices[x][1])

    def get_edges(self):
        return self.edges.keys()


        # def write_textfile(self,filename):
   #     f = open(filename, "wt")  # wt -> write, text-mode
   #     for cl in self._data:
    #        f.write(str(cl.idc) + ',' + cl.name + "\n")

    #    f.close()


def read_textfile(filename):
        k=0
        f = open(filename, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            if k==0:
               n, m = line.split(maxsplit=1, sep=' ')
               g = Graph(int(n))
               k+=1
            else:
                x, y,cost= line.split(maxsplit=2, sep=' ')

                g.add_edge(int(x),int(y),int(cost))

        f.close()
        return g

def ford(g,s,t):
    d=[]
    prev=[]
    nr_vert=g.get_nr_of_vertices()
    for i in range(0,nr_vert):      #initialization
        d.append(999999)
        prev.append("null")

    d[int(s)]=0
    k=0
    cycle=0
    changed =1
    while changed==1:
        changed=0
        for edge in g.get_edges():
            x=int(edge[0])
            y=int(edge[2])
            if d[y]>d[x] + g.get_cost(x,y):
                d[y]=d[x] + g.get_cost(x,y)
                prev[y]=x
                changed=1
        if k > nr_vert-1:                    # check if there is a negative cycle (ford must run at most nr_vert-1 times)
            cycle=1
            break
        k+=1
    if cycle==1:
        print("There is a negative cost cycle!!!")
        return
    cost=d[t]
    result=[]
    node=prev[t]
    if cost!=999999:
        result.append(t)
    while node!="null":                         #reconstruct the path
        result.append(node)
        node=prev[node]
   # result.append(node)
    result.reverse()
    print(result)
    print(cost)
    #print(prev)
    #print(d)
def write_textfile(g,filename):

    f = open(filename, "wt")  # rt -> read, text-mode
    f.write(str(g.get_nr_of_vertices())+" "+ str(g.get_nr_of_edges())+"\n")
    for key in g.edges:
        f.write(str(key[0]) + " " + str(key[2]) + " "+ str(g.get_cost(int(key[0]),int(key[2]))) + "\n")

    f.close()
def print_edges(g):
    for key in g.edges:
        print(key, g.get_cost(int(key[0]),int(key[2])))
def print_graph(g):
    print("Outbound neighborss:")
    for x in g.parse_vertices():
        s = str(x) + ":"

        for y in g.parse_nout(x):
            s = s + " " + str(y)
        print(s)
    print("Inbound neighborss:")
    for x in g.parse_vertices():
        s = str(x) + ":"
        for y in g.parse_nin(x):
            s = s + " " + str(y)
        print(s)

def create_random_graph(n, m):
    g = Graph(n)
    while m > 0:
        x = random.randrange(n)
        y = random.randrange(n)
        if g.is_edge(x, y)==(0,0):
            g.add_edge(x, y,random.randint(2,20))
            m = m - 1
    return g
def print_menu():
    print("0. Exit")
    print("1. Add edge")
    print("2. Remove edge")
    print("3. Add vertex")
    print("4. Remove vertex")
    print("5. Get cost of edge")
    print("6. Set cost of edge")
    print("7. Get nr of vertices")
    print("8. Get nr of edges")
    print("9. Parse all vertices")
    print("10. Parse nin")
    print("11. Parse nout")
    print("12. Print graph")



def start(g):
    while True:
        print("\n")
        print_menu()
        opt = input()
        if opt == "1":
            x = input("Give the x: ")
            y = input("Give the y: ")
            c=input("Give the cost: ")
            g.add_edge(int(x),int(y),int(c))

        elif opt == "2":
            x = input("Give the x: ")
            y = input("Give the y: ")
            g.remove_edge(int(x),int(y))

        elif opt == "3":
            g.add_vertex()
        elif opt == "4":
            x = input("Give the x: ")
            g.delete_vertex(int(x))

        elif opt == "5":
            x = input("Give the x: ")
            y = input("Give the y: ")
            g.get_cost(int(x),int(y))
        elif opt == "6":
            x = input("Give the x: ")
            y = input("Give the y: ")
            n=input("New cost is: ")
            g.set_cost(int(x),int(y),int(n))
        elif opt == "7":
            print(g.get_nr_of_vertices())
        elif opt == "8":
            print(g.get_nr_of_edges())
        elif opt == "9":
            l=g.parse_vertices()
            for i in l:
                print(i)
        elif opt == "10":
            x= input("Give x: ")
            l=g.parse_nin(int(x))
            for i in l:
                print(i)
        elif opt == "11":
            x = input("Give x: ")
            l = g.parse_nout(int(x))
            for i in l:
                print(i)
        elif opt == "12":
            print_graph(g)
        elif opt=="0":
            return
def main():

    #g=read_textfile("random_graph1.txt")
    g=Graph(5)
    g.add_edge(0,2,10)
    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 1)
    g.add_edge(0, 3, -3)
    g.add_edge(3, 4, -4)
    g.add_edge(4, 2, 1)
    g.add_edge(4, 0, -1)
    ford(g,0,2)
    #write_textfile(g,"random_graph2.txt")


main()