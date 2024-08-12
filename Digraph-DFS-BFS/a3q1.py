import sys

n = int(sys.stdin.readline().strip())

while n:
    adjacency = [None]*n
    for i in range(n):
        a_graph = sys.stdin.readline().strip().split()

        adjacency[i] = []
        for j in a_graph:
            adjacency[i].append(int(j))

    print(len(adjacency)-1)
    deleted_arcs = len(adjacency[n-3])
    adjacency.pop(n-3)

    for each_graph in adjacency:
        for node in each_graph:
            if node < (n-3):
                print(node, end=" ")
            elif node == (n-3):
                deleted_arcs += 1
            elif node > (n-3):
                print(node-1, end=" ")
        print()
    print(deleted_arcs)
    n = int(sys.stdin.readline().strip())
print(0)
