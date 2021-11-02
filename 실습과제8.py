def dfs_recur(adj, vtx, visited, id):
    visited[id] = True
    print(vtx[id], end = " ")
    for i in range(len(adj)):
        if adj[id][i] == 1 and not visited[i]:
            dfs_recur(adj,vtx, visited, i)



def dfs(adj, vtx, s):
    n = len(vtx)
    visited = [False]*n
    dfs_recur(adj, vtx, visited, s) 

vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0,1,1,0,0,0,0,0],
          [1,0,0,1,0,0,0,0],
          [1,0,0,1,1,0,0,0],
          [0,1,1,0,0,1,0,0],
          [0,0,1,0,0,0,1,1],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,1],
          [0,0,0,0,1,0,1,0]]
print('DFS', end = '')
print()
dfs(adjMat,vertex,0)
print()

