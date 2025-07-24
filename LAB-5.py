#  Breadth First Search Algorithm

#  Class For BTS Algorithm
class BFS:

    def __init__(self):
        self.visited = {}  # visited nodes tored in dictionary
        self.level = {}     # level of nodes stored
        self.parent = {}    # parent info stored
        self.traversal_output = []
        self.queue = []

    # BFS function
    def BFS2(self,graph,root):
        self.visited = {}  # visited nodes tored in dictionary
        self.level = {}     # level of nodes stored
        self.parent = {}    # parent info stored
        self.traversal_output = []
        self.queue = []
        # initializing the whole nodes 
        for node in graph.keys():
            self.visited[node] = 'No'
            self.level[node]=-1
            self.parent[node]=None
        # BTS algo starts from here
        self.visited[root]='Yes'
        self.level[root]=0
        self.queue.append(root)
        while self.queue:
            pn=self.queue.pop(0)  # pn = parent node
            self.traversal_output.append(pn)
            for node in graph[pn]:
                if self.visited[node]=='No':
                    self.visited[node]='Yes'
                    self.level[node]=self.level[pn]+1
                    self.parent[node]=pn
                    self.queue.append(node)
    def display_graph(self):
        # printing the graph 
        print("\n------------------------------Graph with Nodes----------------------")
        print(self.traversal_output)
    def display_parent(self):
        # printing the parents of each node in the graph 
        print("\n------------------------------Parents of the Nodes----------------------")
        print(self.parent)
    def display_level(self):
        # printing the level of each node in the graph 
        print("\n------------------------------Level of the Nodes----------------------")
        print(self.level)
    def display_path(self):
        # Path of 'G' Node from Root Node
        print("\n------------------------------Path of a Node from Root Node----------------------")
        v=input("Enter the Node to find its path:")
        path=[]
        while v is not None:
            path.append(v)
            v=self.parent[v]
        path.reverse()
        print(path)
    def search_node(self):
        # Search the node
        print("\n------------------------------Search a Node from Graph----------------------")   
        node=input("Enter the node to be searched in the Graph:")
        check=False
        for n in self.traversal_output:
            if n==node:
                check=True
                break       
        if check==True:
            print(node," node is found successfully!")
        else:
            print(node," node is not found!")

#-------------------------------------Samples Graph---------------------------

graph1={
    '0': ['1','4'],
    '1': ['0','2','3','4'],
    '2': ['1','3'],
    '3': ['1','2','4'],
    '4': ['0','1','3']
}

graph2={
    'A':['B','D','E','F'],
    'B':['K','J'],
    'C':[],
    'D':['G'],
    'E':['C','H','I'],
    'F':[],
    'G':[],
    'H':[],
    'I':['L'],
    'J':[],
    'K':['M','N'],
    'L':[],
    'M':[],
    'N':[],
}

#------------------------------Objects using BTS class for Sample Graphs---------------------------

# object of the class
g1=BFS()
g2=BFS()
# Calling the Functions for graph2
g1.BFS2(graph2,'A')
g1.display_graph()
g1.display_parent()
g1.display_level()
g1.display_path()
g1.search_node()

# Calling the Functions for graph1
g1.BFS2(graph1,'0')
g1.display_graph()
g1.display_parent()
g1.display_level()
g1.display_path()







