from itertools import permutations


test = ['박', '사', '이']

t = permutations(test)

for i in t:
    print(i)