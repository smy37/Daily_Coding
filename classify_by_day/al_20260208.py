class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur = 0
        answer = []
        for idx, n in enumerate(target):
            for _ in range(n-cur-1):
                answer.append("Push")
                answer.append("Pop")
            answer.append("Push")
            cur = n
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.buildArray([1, 3], 3))

    explain = """
    Push and Pop operation is needed when numbers is not existed in target. 
    """