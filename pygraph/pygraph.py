class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, start, end, weight=1):
        if start not in self.vertices:
            self.add_vertex(start)
        if end not in self.vertices:
            self.add_vertex(end)
        self.edges.append((start, end, weight))
        self.vertices[start].append((end, weight))

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_edges(self):
        return self.edges

    def get_neighbors(self, vertex):
        return self.vertices.get(vertex, [])

    def depth_first_search(self, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor, _ in reversed(self.get_neighbors(vertex)):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def breadth_first_search(self, start):
        visited = set([start])
        queue = [start]
        result = []

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)
            for neighbor, _ in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result


def create_graph():
    return Graph()
