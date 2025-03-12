import sys
import math

s_n, e_n = map(int, sys.stdin.readline().split())

### 1. 첫번째 접근 방법
    # cri_s = int(math.log2(s_n))
    # cri_e = int(math.log2(e_n))
    # print(s_n.bit_length(), e_n.bit_length())
    # def make_bin(s_cri, e_cri):
    #     s = [1]
    #     t = []
    #     t.append(s)
    #     for i in range(e_cri):
    #         s = s + [j + 1 for j in s]
    #
    #         t.append(s)
    #     t = [item for sub_list in t for item in sub_list]
    #     print(sum(t[s_n-1:e_n]))
    #
    # make_bin(cri_s, cri_e)


### 2. 두번째 접근 방법
def cnt_one_in_bit(n:int):
    if n <= 0:
        return 0
    x = n.bit_length()-1

    pre_cnt = x*(2**(x-1))
    mid_cnt = (n-2**(x)+1)
    rest_cnt = cnt_one_in_bit(n-2**x)

    return int(pre_cnt + mid_cnt + rest_cnt)

print(cnt_one_in_bit(e_n)-cnt_one_in_bit(s_n-1))