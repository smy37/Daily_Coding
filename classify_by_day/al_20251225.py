from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        memory = [False for _ in range(n)]

        for num in nums:
            if memory[num-1]:
                return num
            memory[num-1] = True



if __name__ == "__main__":
    explain = """
    To check duplicated number, I use memory for record using number.
    """