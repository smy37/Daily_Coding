from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        memory = [0 for _ in range(len(temperatures))]
        for idx, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([t, idx])
            else:
                while stack:
                    if stack[-1][0] < t:
                        cur_t, cur_idx = stack.pop()
                        memory[cur_idx] = idx - cur_idx
                    else:
                        break
                stack.append([t, idx])

        return memory


if __name__ == "__main__":
    test_case = [73,74,75,71,69,72,76,73]
    sol = Solution()
    print(sol.dailyTemperatures(test_case))

    explain = """
    Using a stack to update the state helps maintain the required order in the stack.
    """