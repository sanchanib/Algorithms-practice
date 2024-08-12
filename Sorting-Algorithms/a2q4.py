import sys
import math

tosort =[]
for each_line in sys.stdin:
    each_line = each_line.strip()
    if len(each_line) > 1:

        split1 = each_line.split(" ")
        if (len(split1) > 1):
            x = int(split1[1])
            y = int(split1[2])
            split2 = [split1[0], math.sqrt((x**2)+(y**2))]
            tosort.append(split2)
        
    
    elif len(each_line) == 0:
        break


def partition(tosort, low, high):
 
    pivot = tosort[high][1]

    i = low - 1

    for j in range(low, high):
        if tosort[j][1] <= pivot:
 
            i = i + 1

            (tosort[i], tosort[j]) = (tosort[j], tosort[i])

    (tosort[i + 1], tosort[high]) = (tosort[high], tosort[i + 1])

    return i + 1

def quickSort(tosort, low, high):
    if low < high:

        pi = partition(tosort, low, high)
 
        quickSort(tosort, low, pi - 1)
 
        quickSort(tosort, pi + 1, high)
    


quickSort(tosort, 0, len(tosort) - 1)

for i in range(len(tosort)):
    print(tosort[i][0])


