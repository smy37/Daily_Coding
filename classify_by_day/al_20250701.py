import sys

ori_str = sys.stdin.readline().strip()
virus_str = sys.stdin.readline().strip()


s = 0
cri_length = min(len(ori_str), len(virus_str))

for i in range(cri_length):
    if ori_str[s] != virus_str[s]:
        break
    s += 1

e = 0
for i in range(cri_length-1, -1, -1):
    if ori_str[len(ori_str)-1-e] != virus_str[len(virus_str)-1-e]:
        break
    e += 1

if s + e < cri_length:
    print(len(virus_str)-(s+e))
else:
    if len(ori_str) >= len(virus_str):
        print(0)
    else:
        print(len(virus_str)-len(ori_str))


explain = """
처음에는 LCS를 사용하는 문제라고도 생각했지만 해당 문제는 새로 생기는 부분이 연속되어야 한다는 조건 때문에
prefix와 suffix를 구해서 이를 이용해야 했다. xaaaaaaaaaaay 와 caaaaaaaaad 처럼 중간에 아무리 많이 겹쳐도
새로 생기는 부분이 연속되어야 한다는 조건 때문에 해당 문자열 조합에서 중간의 a로 이루어진 부분을 활용할 수 없다.
맨 앞 문자열과 맨 뒤 문자열을 포함해서 한곳에만 연속된 문자열이 들어갈 수 있으므로 prefix와 suffix로 조사하는것이
알맞은 문제인 것이다. 
prefix와 suffix를 구한후에 원래의 문자열과 변환된 문자열 간의 길이 관계를 바탕으로
추가되어야 하는 문자열의 길이가 정해진다.
"""