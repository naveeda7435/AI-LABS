class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, goal):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node == goal:
                print(f"Goal node {goal} found!")
                return True
            if node not in visited:
                print(node)  # Process the node (e.g., print it)
                visited.add(node)
                # Push all unvisited adjacent nodes onto the stack
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

        print(f"Goal node {goal} not found.")
        return False

# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'G')
g.add_edge('E', 'G')

print("Depth First Search starting from node A:")
g.dfs('A', 'G')