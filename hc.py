def backtrack(visited, vertices):
    j = visited[-1]
    visited.pop()
    i = visited[-1]
    j = j + 1
    while j < vertices:
        if visited == []:
            return vertices
        elif i == j or j in visited:
            j = j + 1
        else:
            return i, j
    return i, j
def hamiltonian_cycle(edges, vertices):
    visited = list()
    i, j = 0, 0
    visited.append(0)
    while j < vertices:
        if len(visited) == vertices:
            k = visited[-1]
            if edges[k][0] == 1:
                visited.append(0)
                return visited
            else:
                i, j = backtrack(visited, vertices)
                while j == vertices:
                    i , j = backtrack(visited, vertices)
                
        elif i == j:
            j = j + 1
        elif j in visited:
            j = j + 1
        elif edges[i][j] == 1:
            visited.append(j)
            i = j
            j = 0
        else:
            j = j + 1
    return visited

"""def edge_assign(edges, vertices):
    res = list()
    for i in range(vertices):
        for j in range(i, vertices):
            if i == j:
                edges[i][j] = 0
            else:
                print("any edge b/w", i," and ",j," (1 / 0)")
                ch = int(input())
                if int(ch) == 1:
                    edges[i][j] = 1
                elif int(ch) == 0:
                    edges[i][j] = 0
    for i in range (vertices):
        for j in range(0, i):
            edges[i][j] = edges[j][i]

    res = hamiltonian_cycle(edges, vertices)

    if(len(res) == vertices + 1):
        print(res)
    else:
        print(False)
"""

# vert = int(input("Enter no. of vertices:"))
vert = 5

# edges_matrix = [[0 for x in range(vert)] for x in range(vert)]
edges_matrix = [[0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [0, 0, 1, 1, 0]]

#edge_assign(edges_matrix, vert)
res = list()
res = hamiltonian_cycle(edges_matrix, vert)
if(len(res) == vert + 1):
    print(res)
else:
    print(False)