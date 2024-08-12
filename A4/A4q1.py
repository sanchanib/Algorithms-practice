import sys

check = True
tree_dict = {}

def calculate(current_node,line,tree_dict):
    result = 0
    if line[current_node] == "+":
        for item in tree_dict[current_node]:
            result += calculate(item,line,tree_dict)
        return result
    elif line[current_node] == "*":
        result = 1
        for item in tree_dict[current_node]:
            result *= calculate(item,line,tree_dict)
        return result
    else:
        return int(line[current_node])

for line in sys.stdin:
    if check:
        line = line.strip().split(",")
        for i in range(len(line)):
            try: 
                tree_dict[int(line[i])].append(i)
            except:
                tree_dict[int(line[i])] = [i]
        check = False
    else:
        line = line.strip().split(",")
        result = calculate(tree_dict[-1][0],line,tree_dict)
        tree_dict = {}
        print(result)
        check = True
