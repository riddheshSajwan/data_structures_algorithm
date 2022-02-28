
# iterative approach
def dfs(graph,source):
    visited = []
    stack = []
    stack.append(source)
    while stack:
        currentNode = stack[-1]
        stack.pop()
        if currentNode not in visited:
            print(currentNode,end=" ")
            visited.append(currentNode)
        
        for neighbour in graph[currentNode]:
            if neighbour not in visited:
                stack.append(neighbour)

# recursive approach
def dfs_rec(graph,source,visited=[]):
    if source not in visited:
        print(source,end=" ")
        visited.append(source) 
    for neighbour in graph[source]:
        if neighbour not in visited:
            dfs_rec(graph, neighbour, visited)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

dfs(graph, 'A')
print()
dfs_rec(graph, 'A')