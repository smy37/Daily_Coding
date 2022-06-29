def solution(C):
    cur = 0
    final_log = []
    log = []
    final_log.append(log)
    log_num = 0
    temp = 0
    for i in C:
        if i[0] == "BACK":
            temp = cur-int(i[1])
            if temp <0:
                cur = 0
            else:
                cur = temp
        elif i[0] == "NEXT":
            temp = cur+int(i[1])
            if temp > len(final_log[log_num])-1:
                cur = len(final_log[log_num])-1
            else:
                cur = temp
        elif i[0] == "PUSH":
            final_log[log_num] = final_log[log_num][:cur+1] + [i[1]]
            cur = len(final_log[log_num])-1
        elif i[0] == "OPEN":
            if len(final_log[log_num]) == 0:
                final_log[log_num] = final_log[log_num][:cur+1] + [i[1]]
                cur = len(final_log[log_num])-1
            else:
                final_log.append([])
                log_num +=1
                cur = 0
                temp = 0
                final_log[log_num].append(i[1])
        elif i[0] == 'CHANGE':
            log_num = i[1]
            cur = len(final_log[log_num])-1
    answer = []
    for i in final_log[log_num][::-1]:
        if i not in answer:
            answer = [i]+answer
    return answer

print(solution([["PUSH","www.domain1.com"],["PUSH","www.domain2.com"],["PUSH","www.domain3.com"],["BACK","1"],["BACK","1"],["PUSH","www.domain4.com"]]))
print(solution([["PUSH","www.google.com"],["PUSH","www.yahoo.com"]]))
print(solution([["PUSH", "www.domain1.com"], ["PUSH", "www.domain2.com"], ["OPEN", "www.domain3.com"], \
    ["OPEN", "www.domain3.com"], 	["CHANGE", "0"]]))