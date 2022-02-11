import sys

cri = int(sys.stdin.readline())

def tile_problem(criteria):

    if criteria == 1:
        return 1
    elif criteria == 2:
        return 2

    else:

        x = 1
        y = 1

        for i in range(1, criteria-1):
            z = int(x)
            x = (y + x) % 15746
            y = z % 15746

        return x + y


print(tile_problem(cri)%15746)