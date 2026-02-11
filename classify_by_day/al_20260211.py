class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0 for _ in range(len(prices))]
        stack = []

        for idx, price in enumerate(prices):
            if len(stack) == 0:
                stack.append([idx, price])
            else:
                while stack and stack[-1][1] >= price:
                    i, p = stack.pop()
                    answer[i] = p - price
                stack.append([idx, price])
        for idx, price in stack:
            answer[idx] = price
        return answer