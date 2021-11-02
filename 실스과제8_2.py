from queue import Queue

def bfs(adj, vtx, s):
    queue = Queue()
    queue.put(vtx[s])
    n = len(vtx)
    visited = [False]*n
    visited[s] = True
    while not queue.empty():
        vertex = queue.get()
        print(vertex, end = ' ')
        for i in range(len(adj)):
            if adj[s][i] == 1 and not visited[i]:
                queue.put(vtx[i])
                visited[i] = True
                s = i
                break

vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0,1,1,0,0,0,0,0],
          [1,0,0,1,0,0,0,0],
          [1,0,0,1,1,0,0,0],
          [0,1,1,0,0,1,0,0],
          [0,0,1,0,0,0,1,1],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,1],
          [0,0,0,0,1,0,1,0]]

print('BFS : ', end = "")
bfs(adjMat,vertex,0)
print()