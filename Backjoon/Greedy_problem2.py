import sys

debate_list = []
debate_num = int(sys.stdin.readline().strip())


for i in range(debate_num):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    debate_list.append(temp)


debate_list = sorted(debate_list, key= lambda x : (x[1],x[0]))

cnt = 1
i_1 = debate_list[0][1]

for i in range(1,len(debate_list)):
    if i_1 <= debate_list[i][0]:
        cnt +=1
        i_1 = debate_list[i][1]

print(cnt)