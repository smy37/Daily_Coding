import sys
import string

naming = 'AAAA'
answer = 0
cnt_list = []
cnt = 0
name = []
idx_list = []
for idx, i in enumerate(naming):
    name.append(i)
    if i!='A':
        idx_list.append(idx)

alpha = string.ascii_uppercase
alpha_order = {}
for idx,a in enumerate(alpha):
    alpha_order[a] = idx

if len(naming) == 1:
    print(min(26-alpha_order[naming], alpha_order[naming]))
    sys.exit()

for i in idx_list:
    cnt += min(26-alpha_order[naming[i]], alpha_order[naming[i]])


for idx, value in enumerate(idx_list):
    temp = 0
    temp2 = 0
    if idx < len(idx_list)-1:
        temp += 2*value
        temp += len(naming)-idx_list[idx+1]
        cnt_list.append(temp)
    if idx !=0:
        temp2 += (len(naming)-value)*2 + idx_list[idx-1]
        cnt_list.append(temp2)
if len(idx_list) !=0:
    cnt_list.append(idx_list[-1])
else:
    print(0)
    sys.exit()
cnt_list.append(len(naming)-1)
cnt += min(cnt_list)
answer = cnt
print(answer)