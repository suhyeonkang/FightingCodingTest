
def DFS(graph, start_v, visited=[]):

    visited.append(start_v)

    
    for v in graph[start_v]:
        if v not in visited:
            visited.append(v)
            DFS(graph, v, visited)

    return visited        

