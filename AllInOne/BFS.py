from collections import deque

def BFS(graph, start_v):

    visited = []

    q = deque()
    q.append(start_v)
    visited.append(start_v)

    while q :
        current_v = q.popleft()

        for v in graph[current_v]:
            if v not in visited :
                visited.append(v)  ## 현재 vertex에서 연결된 vertex를 모두 방문
                q.append(v) ## 현재 vertex랑 연결된 vertex도 방문해서 봐야되니까 큐에 삽입 

    return visited            


    

