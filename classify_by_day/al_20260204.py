from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        cur = []
        for _ in range(numRows):
            if len(cur) < 2:
                cur = cur + [1]

                answer.append(cur)
            else:
                new_cur = [1]
                for i in range(len(cur)-1):
                    new_cur.append(cur[i]+cur[i+1])
                new_cur.append(1)
                cur = new_cur
                answer.append(cur)

        return answer

if __name__ == "__main__":
    test_case = 5
    sol = Solution()
    print(sol.generate(test_case))
