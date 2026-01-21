from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def check_palin(string):
            for i in range(len(string) // 2):
                if string[i] == string[-(i + 1)]:
                    continue
                else:
                    return False
            return True

        def dfs(idx, record):
            cur_s = s[idx]
            if idx == len(s) - 1:
                if check_palin(record[-1]):
                    answer.append(record + [cur_s])
                if check_palin(record[-1] + cur_s):
                    temp = record[:]
                    temp[-1] += cur_s
                    answer.append(temp)
            else:
                if len(record) == 0:
                    record.append(cur_s)
                    dfs(idx + 1, record)
                else:
                    ori = record[-1]
                    temp = record[-1] + cur_s

                    if check_palin(temp) or idx < len(s)//2+1:
                        record[-1] = temp
                        dfs(idx + 1, record)
                        record[-1] = ori
                    if check_palin(record[-1]):
                        dfs(idx + 1, record + [cur_s])

        if len(s) == 1:
            answer.append([s])
        else:
            dfs(0, [])
        return answer


sol = Solution()
print(sol.partition("efe"))