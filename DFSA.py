graph = {
 'B':['C','D'],
 'C':['A','E'],
 'D':['G','F'],
 'A':['H'],
 'E':['I'],
 'G':['J'],
 'F':['H'],
 'H':[],
 'I':[],
 'J':[],
 'K':[],
}
visited = set()
def dfs(visited,graph,node):
  if node not in visited:
  print(node,end=" ")
  visited.add(node)
  for neighbour in graph[node]:
      dfs(visited,graph,neighbour)

print("Following is the Depth First Search")