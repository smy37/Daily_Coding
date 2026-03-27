import sys 

N = int(sys.stdin.readline())
work_list = []

for _ in range(N):
    duration, end_limit = map(int, sys.stdin.readline().split())
    
    work_list.append([duration, end_limit])

work_list.sort(key = lambda x : x[1])



answer = work_list[0][1]-work_list[0][0]
cur = work_list[0][1]
if answer <-1:
    print(-1)
    sys.exit()
for during, limit in work_list[1:]:   
    if cur + during > limit:    
        mod_value = (cur+during)-limit
        if answer - mod_value < 0 :
            print(-1)
            sys.exit()
        else:
            answer -= mod_value
            cur=limit
    else:
        cur += during
        
print(answer)
