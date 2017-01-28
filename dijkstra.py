#!/usr/bin/python
from Queue import PriorityQueue as PQ
V = ['a', 'b', 'c', 'd', 'e']
E = [ {'from': 'a', 'to': 'b', 'dist': 2},
      {'from': 'a', 'to': 'c', 'dist': 8},
      {'from': 'a', 'to': 'd', 'dist': 5},
      {'from': 'b', 'to': 'c', 'dist': 1},
      {'from': 'c', 'to': 'e', 'dist': 3},
      {'from': 'd', 'to': 'e', 'dist': 4}
    ]

class Graph(object):
    def __init__(self, vertices, edges):
        self.adj_matrix = {}
        for v in vertices:
            self.adj_matrix[v] = []
        for e in edges:
            self.adj_matrix[e['from']].append( (e['to'], e['dist']) )

    def get_neighbors(self, node):
        return self.adj_matrix[node]


def dijkstra(myg, start):
    distance_to = {i: -1 for i in V}
    distance_to[start] = 0

    frontier = PQ()
    frontier.put(start)

    while not frontier.empty():
        u = frontier.get(False)
        for v in myg.get_neighbors(u):
            if (distance_to[v[0]] == -1 or v[1] + distance_to[u] < distance_to[v[0]]):
                distance_to[v[0]] = v[1] + distance_to[u]
            frontier.put(v[0])
    return distance_to

def main():
    mygraph = Graph(V, E)

    for v in V:
        distance_from_v = dijkstra(mygraph, v)
        print("Perfoming Dijkstra's algorithm on {0}".format(v))
        for x in distance_from_v:
            if distance_from_v[x] < 0:
                print("{0} is not reachable from {1}".format(x, v))
            elif x != v:
                print("Distance from {0} to {1} is: {2}".format(v, x, distance_from_v[x]))
        print("")

if __name__ == "__main__":
    main()
