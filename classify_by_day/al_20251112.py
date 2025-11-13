import sys

num_l = {"M": 1000, "CM":900, "D":500, "CD":400, "C":100, \
         "XC":90, "L": 50, "XL":40, "X":10, "IX":9, \
         "V":5, "IV":4 , "I": 1}

str_1 = sys.stdin.readline().strip()
str_2 = sys.stdin.readline().strip()

num_1 = 0
idx = 0
while idx < len(str_1):
    if idx < len(str_1)-1:
        s1, s2 = str_1[idx], str_1[idx+1]
        if num_l[s1] < num_l[s2]:
            num_1 += num_l[s1+s2]
            idx = idx+1
        else:
            num_1 += num_l[s1]
    else:
        num_1 += num_l[str_1[idx]]
    idx += 1


num_2 = 0
idx = 0
while idx < len(str_2):
    if idx < len(str_2)-1:
        s1, s2 = str_2[idx], str_2[idx+1]
        if num_l[s1] < num_l[s2]:
            num_2 += num_l[s1+s2]
            idx = idx+1
        else:
            num_2 += num_l[s1]
    else:
        num_2 += num_l[str_2[idx]]
    idx += 1

total_num = num_1+num_2
print(total_num)

answer = ""
while total_num > 0:
    for k in num_l:
        if total_num >= num_l[k]:
            answer += k
            total_num-= num_l[k]
            break

print(answer)

explain = """
문자열에 상응하는 수를 딕셔너리에 기록해 두었다가 큰 수부터 차례대로 문자열을 할당한다. 
문제어서 주어진 조건으로 그리디하게 큰수부터 문자열을 할당하면 정답이 된다. 
"""