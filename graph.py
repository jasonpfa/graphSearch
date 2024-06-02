from collections import deque
from queue import PriorityQueue


def bfs(graph, start, finish):
    queue = deque([start])
    parent = {}
    parent[start] = start
    while queue:
        curr = queue.popleft()

        for adj in graph[curr]:
            if adj[0] == finish:
                parent[adj[0]] = curr
                print_path(parent, adj[0], start)
                return

            if adj[0] not in parent:
                parent[adj[0]] = curr
                queue.append(adj[0])
    print("No path found.")


def dijkstra(graph, start, finish):
    visited = set()
    dist = {start: 0}
    parent = {start: None}
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        while not queue.empty():
            _, vertex = queue.get()
            if vertex not in visited:
                break
        else:
            break
        visited.add(vertex)
        if vertex == finish:
            break
        for adj, dis in graph[vertex]:
            if adj in visited:
                continue
            old_cost = dist.get(adj, float('inf'))
            new_cost = dist[vertex] + int(dis)
            if new_cost < old_cost:
                queue.put((new_cost, adj))
                dist[adj] = new_cost
                parent[adj] = vertex
    print_path(parent, finish, start)


def print_path(parent, finish, start):
    path = [finish]
    while finish != start:
        finish = parent[finish]
        path.insert(0, finish)
    print(path)


def printGraph(graph):
    for key, item in graph.items():
        print(key, "--> ", end="")
        for i in range(len(item)):
            if i != len(item) - 1:
                print(item[i][0], ",", end="", sep="")
            else:
                print(item[i][0])


def main():
    fileVert = open("RomaniaVertices.txt", "r")
    fileEdge = open("RomaniaEdges.txt", "r")
    graph = {}
    while True:
        lineVert = fileVert.readline()
        lineVert = lineVert.strip()
        if not lineVert:
            break
        graph[lineVert] = []

    lineEdge = fileEdge.readline()
    lineEdge = lineEdge.rstrip("\n").split(",")
    for lineVert in graph:
        while lineVert == lineEdge[0]:
            graph[lineVert].append(list([lineEdge[1], lineEdge[2]]))
            graph[lineEdge[1]].append(list([lineEdge[0], lineEdge[2]]))
            lineEdge = fileEdge.readline()
            lineEdge = lineEdge.rstrip("\n").split(",")
    fileVert.close()
    fileEdge.close()

    printGraph(graph)
    print("BFS:")
    bfs(graph, "Arad", "Sibiu")
    bfs(graph, "Arad", "Craiova")
    bfs(graph, "Arad", "Bucharest")
    print("Dijkstra:")
    dijkstra(graph, "Arad", "Bucharest")

main()
