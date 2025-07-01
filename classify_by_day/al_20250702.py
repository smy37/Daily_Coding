import sys 

w, s = map(int, sys.stdin.readline().split())
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()


### First Approach
# target = []
# for i in W:
#     target.append(i)
# target.sort()

# result = 0

# for i in range(s-w+1):
#     temp = sorted([j for j in S[i:i+w]])
#     if temp == target:
#         result += 1

# print(result)

### Second Approach
def change_alpha2num(c: str):
    if c.isupper():
        return ord(c)-ord('A')+26
    else:
        return ord(c)-ord('a')

answer = 0
s_idx = 0
w_dict = [0]*52
s_dict = [0]*52

for c in W:
    str_num = change_alpha2num(c)
    w_dict[str_num] += 1

for c in S:
    str_num = change_alpha2num(c)
    s_dict[str_num] += 1

    if sum(s_dict) == w:
        if w_dict == s_dict:
            answer += 1

        past_num = change_alpha2num(S[s_idx])
        s_dict[past_num] -= 1
        s_idx += 1
        
print(answer)


explain = """
첫번재 시도에서는 주어지는 문자열에서 첫번째 부터 단어 길이만큼 추출해 정렬하여 
원래의 단어 배열과 비교하는 방식을 사용하였다. 이는 시간초과가 발생하였고
마찬가지로 단어를 시작부터 오른쪽으로 옮기지만 이전 결과에서 처음 문자에 해당하는 
값만 없애주는 것으로 업데이트 해주는 방식으로 바꿨다. 
슬라이딩 윈도우 기법에서 오른쪽으로 이동할 때, 기존의 가장 왼쪽 값이 사라짐으로써 
영향을 주는 것을 반영하는게 중요하다고 생각된다.
"""