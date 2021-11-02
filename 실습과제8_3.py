def dfs_cc(adj, color, vertex, visited, s):
        visited[s] = True
        color.append(vertex[s])
        for i in range(len(adj)):
            if adj[s][i] == 1 and not visited[i]:
                dfs_cc(adj,color, vertex, visited, i)


def find_connected_component(adj, vtx):
    n = len(vtx)
    visited = [False]*n
    colorList = []
    visited[0] = True
    for vt in  range(len(adj)):
        if not visited[vt]:
            color = dfs_cc(adj, [], vtx, visited, 0)
            colorList.append(color)
    return len(colorList)

def find_bridges(adj, vtx):
    n = len(vtx)
    count = 0
    for i in range(n): 
        for j in range(i+1,n):
            if adj[i][j] != 0:
                adj[i][j] = adj[j][i] = 0
                if find_connected_component(adj, vtx) > 1:
                    print(find_connected_component(adj, vtx))
                    count += 1
                    print(" Bridge%d: (%s,%s)"%(count, vtx[i], vtx[j]))
                adj[i][j] = adj[i][j] = 1
    return count

vertex = ['A','B','C','D','E','F']
adjMat = [[0,1,0,1,0,0],
          [1,0,1,1,1,0],
          [0,1,0,0,0,1],
          [1,1,0,0,1,0],
          [0,1,0,1,0,0],
          [0,0,1,0,0,0]]

print('find_bridges : ')
find_bridges(adjMat,vertex)
print()