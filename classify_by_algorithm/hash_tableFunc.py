def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    bit1 = 0

    for i in data[row_begin-1]:
        bit1 += i%row_begin

    for i in range(row_begin, row_end):
        bit2 = 0
        for j in data[i]:
            bit2 += j%(i+1)
        bit1 = bit1^bit2

    answer = bit1
    return answer



if __name__ == "__main__":
    print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]] , 2, 2, 3), 4)