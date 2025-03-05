def getMergedLineSegments(lineSegments):
    # Write your code here
    ls = sorted(lineSegments)
    answer = []
    s, e = ls[0][0], ls[0][1]
    if len(ls) == 1:
        answer.append(ls[0])
        return answer
    for i in range(1, len(ls)):
        t = ls[i]
        if t[0] <= e:
            if t[1] <= e:
                continue
            elif t[1] > e:
                e = t[1]
        elif t[0] > e:
            answer.append([s,e])
            s, e = t[0], t[1]
    return answer

a = [[6,9], [2,3],[9,11], ]
print(getMergedLineSegments(a))