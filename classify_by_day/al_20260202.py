class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cur_min = 1
        memory = {}
        for n in nums:
            if cur_min == n and n > 0:
                cur_min += 1
                while cur_min in memory:
                    cur_min += 1
            memory[n] = True

        return cur_min

if __name__ == "__main__":
    test_case = [1, 1]
    sol = Solution()
    print(sol.firstMissingPositive(test_case))

    explain = """
    Update the minimum positive value while iterating through the for loop.
    """
