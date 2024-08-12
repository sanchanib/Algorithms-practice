import sys

from collections import deque

def bfs(adj, v):
    distance = [-1]*n
    distance[v] = 0
    v_queue = deque()
    v_queue.append(v)
    index = 0
    while v_queue:
        front=v_queue.popleft()
        for each in adj[front]:
            if distance[each]==-1:
                distance[each]=distance[front]+1
                v_queue.append(each)
    maximum = max(distance)
    for i in range(n):
      if distance[i] == maximum and i > index:
        index = i
    return maximum, index

n = int(sys.stdin.readline().strip())
while n:
    adjacency=[None]*n
    for i in range(n):
        a_graph = sys.stdin.readline().strip().split()

        adjacency[i] = []
        for j in a_graph:
            adjacency[i].append(int(j)) 
    maximum_distance, lowest_index = bfs(adjacency, 1)
    print(maximum_distance, lowest_index)
    n = int(sys.stdin.readline().strip())
