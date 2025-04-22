import sys
import math

num = int(sys.stdin.readline())

def dot(node_1, node_2):
    return (node_1[0]*node_2[0]+node_1[1]*node_2[1])/(math.sqrt(node_1[0]**2+node_1[1]**2)*math.sqrt(node_2[0]**2+node_2[1]**2))

def product(node_1, node_2):
    return node_1[0]*node_2[1]-node_1[1]*node_2[0]

node_list = []

for i in range(num):
    node_list.append(list(map(int,sys.stdin.readline().strip().split(' '))))

node_list = sorted(node_list, key = lambda x : [x[1], x[0]])
c_x, c_y = node_list[0][0], node_list[0][1]
node_list = node_list[1:]


node_list = sorted(node_list, key = lambda x: round(dot([1,0],[x[0]-c_x, x[1]-c_y]),10), reverse= True)

convex_stack = []

convex_stack.append([c_x, c_y])
convex_stack.append(node_list[0])

for i in range(1, len(node_list)):
    third = node_list[i]
    second = convex_stack.pop()
    first = convex_stack.pop()

    node_1 = [second[0]-first[0], second[1]-first[1]]
    node_2 = [third[0]-second[0], third[1]-second[1]]

    while product(node_1, node_2) <0:
        second = first
        first = convex_stack.pop()
        node_1 = [second[0] - first[0], second[1] - first[1]]
        node_2 = [third[0] - second[0], third[1] - second[1]]
    if product(node_1, node_2) == 0:
        convex_stack.append(first)
        convex_stack.append(third)
    else:
        convex_stack.append(first)
        convex_stack.append(second)
        convex_stack.append(third)

print(len(convex_stack))