class Knoten(object):
    def _init_(self, name, connections=None):
        self.name=name
        self.connections=[]
        if connections is not None:
            self.connections.update(connections)


knoten = [
    Knoten("Munich", {"Cologne": 1, "Dresden": 1}),
    Knoten("Hamburg", {"Berlin": 1}),
    Knoten("Cologne", {"Stuttgart": 1, "Berlin": 1}),
    Knoten("Berlin", {"Hamburg": 1, "Cologne": 1}),
    Knoten("Stuttgart", {"Cologne": 1})
]


def shortest_path(start,end):
    P = _dijkstra(start)
    path, node = [], end
    while not(node == start):
        if path.count(node):break
        path.append(node)
        node = P[node]
        return [start] + list(reversed(path))


def _dijkstra(start):
    D, P = {}, {}
    for knot in knoten:
        D[knot.name], P[knot.name] = float("inf"), None
    D[start] = 0
    unseen_nodes = list[knoten]
    while unseen_nodes:
        shortest = min(unseen_nodes, key=lambda node:D[node.name])
        unseen_nodes.remove(shortest)
        for neighbour, distance in shortest.connections.items():
            if neighbour not in [node.name for node in unseen_nodes]:
                continue
            if D[shortest.name] + distance < D[neighbour]:
                D[neighbour] = D[shortest.name] + distance
                P[neighbour] = shortest.name
    return P


print(shortest_path("Munich", "Hamburg"))




