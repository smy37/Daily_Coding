import sys

cri = ["100+1+", "01"]

T = int(sys.stdin.readline())

for _ in range(T):
    string = sys.stdin.readline().strip()
    cur = 0
    flag = True
    while cur <= len(string)-1:
        if string[cur:cur+2] == "10":
            cur += 2
            if cur > len(string)-1 or string[cur] != "0":
                flag = False
                break

            for i in range(cur, len(string)):
                if string[i] == "1":
                    cur = i
                    break

            if cur > len(string)-1 or string[cur] != "1":
                flag = False
                break

            for i in range(cur, len(string)):
                if string[i] == "0":
                    cur = i
                    break
            if cur == len(string)-1:
                break
        elif string[cur:cur+2] == "01":
            cur += 2
        else:
            if string[cur-1:cur+1] == "10":
                cur = cur-1
                continue
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
