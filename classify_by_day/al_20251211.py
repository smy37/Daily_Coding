from typing import List
from collections import deque
class Solution():
    def coinChang(selfself, coins: List[int], amount: int)->int:
        dp = [float("inf") for _ in range(len(coins))]
        dp[0] = 0
        for i in range(len(dp)):
            for c in coins:
                if i+c <= amount:
                    dp[i+c] = min(dp[i+c], dp[i]+1)

        answer = dp[-1] if dp[-1] != float("inf") else -1

        return answer

    # def coinChange(selfself, coins: List[int], amount: int) -> int:
    #     answer = float("inf")
    #     dq = deque()
    #     for c in coins:
    #         dq.append([c, 1])
    #
    #     while dq:
    #         cur_coin, cur_num = dq.popleft()
    #         if cur_coin == amount:
    #             answer = min(answer, cur_num)
    #             continue
    #         for c in coins:
    #             if cur_coin + c <= amount:
    #                 dq.append([cur_coin + c, cur_num + 1])
    #
    #     answer = answer if amount != 0 else 0
    #     answer = answer if answer != float("inf") else -1
    #     return answer


if __name__ == "__main__":
    test_case = [1,2,5]
    amount = 11
    sol = Solution()
    print(sol.coinChang(test_case, amount))

    explain = """
    BFS can solve this problem, but it exceeds the memory limit. The key idea is to treat the amount as the memory state.
    """