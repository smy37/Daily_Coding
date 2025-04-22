# class FenwickTree:
#     def __init__(self, size):
#         self.size = size
#         self.tree = [0] * (size + 1)
#
#     def update(self, i, delta):
#         while i <= self.size:
#             self.tree[i] += delta
#             i += i & -i
#
#     def query(self, i):
#         s = 0
#         while i:
#             s += self.tree[i]
#             i -= i & -i
#         return s
#
# def solution(N, P1, P0, Connect):
#     coords = sorted(list(set(P1 + P0)))
#     coord_map = {v: i + 1 for i, v in enumerate(coords)}
#     events = []
#     for i in range(N):
#         start_v = min(coord_map[Connect[i][0]], coord_map[Connect[i][1]])
#         end_v = max(coord_map[Connect[i][0]], coord_map[Connect[i][1]])
#         events.append([start_v, 0, i])
#         events.append([end_v, 1, i])
#     events.sort()
#
#     BIT = FenwickTree(len(coords))
#     answer = [0] * N
#     for x, event_type, idx in events:
#         if event_type == 0:  # Start of a segment
#             answer[idx] = BIT.query(x - 1)
#         else:  # End of a segment
#             BIT.update(x, 1)
#
#     return [a % 1007 for a in answer]
#
# # Test cases
# N1, P1, P2, Connect1 = 4, [1, 6, 3, 18], [7, 14, 8, 3], [[1, 7], [6, 14], [3, 8], [18, 3]]
# print(solution(N1, P1, P2, Connect1))  # [0, 0, 0, 3]
#
# N2, P1, P2, Connect2 = 4, [1, 2, 3, 4], [4, 3, 2, -1], [[1, 4], [2, 3], [3, 2], [4, -1]]
# print(solution(N2, P1, P2, Connect2))  # [0, 1, 3, 6]
#
# N3, P1, P2, Connect3 = 4, [1, 2, 3, 4], [4, 3, 2, 1], [[1, 4], [2, 3], [3, 2], [4, 1]]
# print(solution(N3, P1, P2, Connect3))  # [0, 1, 3, 6]
#
#
#
# def update(bit, n, index, val):
#     while index <= n:
#         bit[index] += val
#         index += index & -index
#
# def query(bit, index):
#     sum = 0
#     while index:
#         sum += bit[index]
#         index -= index & -index
#     return sum
#
# def count_inversions(arr):
#     MAX_VAL = max(arr) + 1
#     bit = [0] * (MAX_VAL + 1)
#     inv_count = 0
#     for a in arr:
#         inv_count += query(bit, MAX_VAL) - query(bit, a)
#         update(bit, MAX_VAL, a, 1)
#         print(inv_count)
#     return inv_count

# print(count_inversions([1, 9, 5, 4, 3]))
#
#
#
#
#
# index = 2
# print()
# print(index&-index)
# index-= index&-index
# print(index)
from typing
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, index, val):
        while index <= self.size:
            self.bit[index] += val
            index += index & -index

    def query(self, index):
        res = 0
        while index:
            res += self.bit[index]
            index -= index & -index
        return res

def solution(N, P1, P0, connect):
    events = []
    for i in range(N):
        a, b = connect[i]
        events.append((min(a,b), i, 1))  # starting point of line segment
        events.append((max(a, b), i, -1))  # ending point of line segment

    # Sort events based on x-coordinate
    events.sort()

    count = 0  # number of intersections
    active = set()  # set to keep track of active line segments
    result = [0] * N  # array to store results

    for x, i, t in events:
        if t == 1:  # if starting point of line segment
            for j in active:
                if max(P1[i], P1[j]) < min(P0[i], P0[j]) or max(P1[j], P1[i]) < min(P0[j], P0[i]):
                    continue
                result[i] += 1
                result[j] += 1
            active.add(i)
        else:
            active.remove(i)

        count += len(active) * t

    # Modulo operation for each count in the result
    for i in range(N):
        result[i] = (result[i] - 1 + 1007) % 1007  # subtracting 1 as every line intersect with itself

    return result


# Test the function with the example provided
print(solution(4, [4, 2, 7, 1], [1, 5, -1, 3], [[4, 1], [2, 5], [7, -1], [1, 3]]))


# Test cases
N1, P1, P2, Connect1 = 4, [1, 6, 3, 18], [7, 14, 8, 3], [[1, 7], [6, 14], [3, 8], [18, 3]]
print(solution(N1, P1, P2, Connect1))  # [0, 0, 0, 3]

N2, P1, P2, Connect2 = 4, [1, 2, 3, 4], [4, 3, 2, -1], [[1, 4], [2, 3], [3, 2], [4, -1]]
print(solution(N2, P1, P2, Connect2))  # [0, 1, 3, 6]

N3, P1, P2, Connect3 = 4, [1, 2, 3, 4], [4, 3, 2, 1], [[1, 4], [2, 3], [3, 2], [4, 1]]
print(solution(N3, P1, P2, Connect3))  # [0, 1, 3, 6]