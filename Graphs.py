import  heapq
from tokenize import endpats


class Graphs:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""

        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} ->{neighbours}\n"

        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)

        else:
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def neighbour(self,node):
        return self.adj_list.get(node,set())

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        return order

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())


    def dijkstra(self,start):
        distances = {node:float('inf') for node in self.adj_list}
        distances[start] = 0
        visited = set()
        min_heap = [(0,start)]

        while min_heap:
            current, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor in self.adj_list[current_node]:
                if isinstance(neighbor,tuple):
                    neighbor_node, weight = neighbor
                else:
                    neighbor_node = neighbor
                    weight = 1

                distance = current + int(weight)
                if distance < distances[neighbor_node]:
                    distances[neighbor_node] = distance
                    heapq.heappush(min_heap,(distance,neighbor_node))

        return distances

    def shortest_path(self,start,end):
        distances = {node:float('inf') for node in self.adj_list}
        prev_node = {node:None for node in self.adj_list}
        distances[start]=0
        min_heap = [(0,start)]

        while min_heap:
            current_dis, current_node = heapq.heappop(min_heap)

            if current_node == end:
                break

            for neighbor in self.adj_list[current_node]:
                if isinstance(neighbor,tuple):
                    neighbor_node,weight = neighbor
                else:
                    neighbor_node = neighbor
                    weight = 1

                distance = current_dis + int(weight)

                if distance < distances[neighbor_node]:
                    distances[neighbor_node] =  distance
                    prev_node[neighbor_node] = current_node
                    heapq.heappush(min_heap,(distance,neighbor_node))

        path = []
        current = end

        while current is not None:
            path.insert(0,current)
            current = prev_node[current]

        if distances[end] == float('inf'):
            return [], None

        return path,distances[end]
if __name__ == "__main__":
    graph_ge = Graphs(directed=True)
    graph_ge.add_edge("A", "B", 2)
    graph_ge.add_edge("A", "J", 2)
    graph_ge.add_edge("A", "C", 3)
    graph_ge.add_edge("A", "D", 4)
    graph_ge.add_edge("B", "D", 4)
    graph_ge.add_edge("B", "C", 7)
    graph_ge.add_edge("D", "C", 7)

    print(graph_ge)
    print("BREADTH FIRST SEARCH: \n")
    print(graph_ge.bfs("A"))
    print("DEPTH FIRST SEARCH: \n")
    print(graph_ge.bfs("A"))

    print ("DIJKSTRA DISTANCES: \n")
    distances = graph_ge.dijkstra("A")
    print(distances)

    print("SHORTEST DISTANCE (A-D):\n")
    path,cost = graph_ge.shortest_path("A","D")
    print(f" Path: {path}, Cost: {cost}")