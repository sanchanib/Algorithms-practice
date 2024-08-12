import sys
import math
import heapq

check = True
line = sys.stdin.readline().strip().split(",")

def dijkstra(adjacency_list, coordinates, source, final):
    num_nodes = len(adjacency_list)
    distances = [float('inf')] * num_nodes
    distances[source] = 0
    dist = []
    neg = []
    heapq.heappush(dist, 0)
    heapq.heappush(neg, source)

    while dist:
        current_node = heapq.heappop(neg)
        remove = heapq.heappop(dist)

        if current_node == final:
            return distances[final]

        for neighbour in adjacency_list[current_node]:
            neighbour_coords = coordinates[neighbour]
            current_coords = coordinates[current_node]
            
            neighbour_distance = ((neighbour_coords[0] - current_coords[0]) ** 2 + (neighbour_coords[1] - current_coords[1]) ** 2) ** 0.5

            if ((distances[current_node] + neighbour_distance) < (distances[neighbour])):
                distances[neighbour] = distances[current_node] + neighbour_distance
                temp = [distances[neighbour], neighbour]
                heapq.heappush(dist, distances[neighbour])
                heapq.heappush(neg, neighbour)
    return (-1)

while check:
    n = int(line[0])
    boulders = line[1:]
    pairs = [[float(boulders[i]), float(boulders[i+1])] for i in range(0, len(boulders), 2)]
    adj_list = []

    for i in range(len(pairs)):
        adj_list.append([])

    for i in range(len(adj_list)):
        point = pairs[i]
        for j in range(len(pairs)):
            if j == i:
                pass

            cur = pairs[j]
            xdiff = abs(cur[0] - point[0])
            ydiff = abs(cur[1] - point[1])
            dist = math.sqrt(xdiff * xdiff + ydiff * ydiff)

            if dist <= 100:
                adj_list[i].append(j)

    dist = dijkstra(adj_list, pairs, 0, len(pairs) - 1)

    if dist == -1.00:
        print(-1)
    else:
        print('{:.2f}'.format(dist))

    line = sys.stdin.readline().strip().split(",")

    if line == ['']:
        check = False
    else:
        n = float(line[0])           
