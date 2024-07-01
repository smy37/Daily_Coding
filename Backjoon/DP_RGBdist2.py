# import sys
#
# N = int(sys.stdin.readline())
# board = []
# for i in range(N):
#     temp = list(map(int, sys.stdin.readline().split()))
#     board.append(temp)
# answer = 1000*1000
# if N == 1:
#     print(board[0][0])
#     sys.exit()
# for x in range(3):
#     s = x
#     cur_l = board[0][:]
#     for j in range(3):
#         if j != s:
#             cur_l[j] += 1000*1000
#     s_l = cur_l
#     for i in range(1, N-1):
#         cur_l = board[i][:]
#
#         sort_l = sorted(enumerate(s_l), key = lambda x : x[1])
#         first = sort_l[0][0]
#         second = sort_l[1][0]
#
#         for j in range(3):
#             if j == first:
#                 cur_l[j] += s_l[second]
#             else:
#                 cur_l[j] += s_l[first]
#
#         s_l = cur_l
#     cur_l = board[N-1][:]
#     cur_l[s] += 1000*1000
#     sort_l = sorted(enumerate(s_l), key = lambda x : x[1])
#     first = sort_l[0][0]
#     second = sort_l[1][0]
#
#     for j in range(3):
#         if j == first:
#             cur_l[j] += s_l[second]
#         else:
#             cur_l[j] += s_l[first]
#     answer = min(answer, min(cur_l))
#
# print(answer)

class MySubClass:
    def __init__(self, weight, length, depth):
        self.a = weight
        self.b = length
        self.c = depth
class MySubClass2:
    def __init__(self, property, color, size):
        self.d = property
        self.e = color
        self.f = size
class MyClass:
    def __init__(self, **args):
        self.A = MySubClass(**args['s1'])
        self.B = MySubClass2(**args['s2'])


nested_dict = {'s1': {'weight': 78, 'length': 30, 'depth': 58}, 's2': {'property': 'concrete', 'color': "black",'size': "XL"}}


new_ins = MyClass(**nested_dict)

print(new_ins.A.a)
print(new_ins.A.b)
print(new_ins.A.c)
print(new_ins.B.d)
print(new_ins.B.e)
print(new_ins.B.f)