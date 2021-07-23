def bfs(graph,source):
    visited = []
    queue = []
    visited.append(source)
    queue.append(source)
    while queue:
        currentNode = queue.pop(0)
        print(currentNode, end = " ")
        for neighbour in graph[currentNode]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

bfs(graph, 'A')