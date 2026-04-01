import sys

cri = ["100+1+", "01"]

T = int(sys.stdin.readline())

for _ in range(T):
    # string = sys.stdin.readline().strip()
    # cur = 0
    # flag = True
    # while cur <= len(string)-1:
    #     if string[cur:cur+2] == "10":
    #         cur += 2
    #         if cur > len(string)-1 or string[cur] != "0":
    #             flag = False
    #             break
    #
    #         for i in range(cur, len(string)):
    #             if string[i] == "1":
    #                 cur = i
    #                 break
    #
    #         if cur > len(string)-1 or string[cur] != "1":
    #             flag = False
    #             break
    #
    #         for i in range(cur, len(string)):
    #             if string[i] == "0":
    #                 cur = i
    #                 break
    #         if cur == len(string)-1:
    #             break
    #     elif string[cur:cur+2] == "01":
    #         cur += 2
    #     else:
    #         if string[cur-1:cur+1] == "10":
    #             cur = cur-1
    #             continue
    #         flag = False
    #         break
    # if flag:
    #     print("YES")
    # else:
    #     print("NO")

    s = sys.stdin.readline().strip()
    idx = 0
    flag = True
    while idx < len(s):
        if s[idx:idx+3] == "100":
            for i in range(idx+3, len(s)):
                if s[i] == "1":
                    idx = i
                    break
            else:
                flag = False
                break
            for i in range(idx+1, len(s)):
                if s[i] == "0":
                    break
            else:
                break
            if i > idx+1 and s[i-1:i+2] == "100":
                idx = i-1
            elif s[i:i+2] == "01":
                idx = i
            else:
                flag = False
                break
        elif s[idx:idx+2] == "01":
            idx = idx + 2
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")