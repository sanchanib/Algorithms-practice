import sys

def dfs(node, graph, visited, seen, count, time, back_arcs, cross_arcs):
    visited[node] = True
    seen[node] = time
    time += 1

    for the_next in graph[node]:
        if not visited[the_next]:
            seen,count,time,back_arcs,cross_arcs = dfs(the_next,graph,visited,seen,count,time,back_arcs,cross_arcs)
        else:
            if (count[the_next]!=0) and (seen[the_next] < seen[node]):
                cross_arcs += 1
            elif seen[the_next] < seen[node]:
                back_arcs += 1
    count[node] = time
    time += 1
    return seen, count, time, back_arcs, cross_arcs

n = int(sys.stdin.readline().strip())
while n:
    adjacency = [None]*n
    for i in range(n):
        a_graph = sys.stdin.readline().strip().split()

        adjacency[i] = []
        for j in a_graph:
            adjacency[i].append(int(j))
            
    time = 0
    visited = [False] * n
    seen= [0] * n
    count = [0] * n
    back_arcs = 0
    cross_arcs = 0

    for node in range(n):
        if not visited[node]:
            seen,count,time,back_arcs,cross_arcs = dfs(node,adjacency,visited,seen,count,time,back_arcs,cross_arcs)
    print(back_arcs, cross_arcs);
    n = int(sys.stdin.readline().strip())
