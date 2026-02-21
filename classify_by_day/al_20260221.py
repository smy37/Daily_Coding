import math

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        length = len(s)
        group_num = int(math.ceil(length / k))
        first_num = length % k
        if first_num == 0:
            first_num = k

        answer = [s[:first_num]]

        idx = first_num
        for _ in range(group_num - 1):
            answer.append(s[idx:idx + k])
            idx += k

        return "-".join(answer)

