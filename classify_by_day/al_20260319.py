from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0

        left = 0

        for i, h in enumerate(height[1:]):
            if height[left] <= h:
                if height[left] > 0:
                    for idx in range(left+1, i+1):
                        answer += height[left] - height[idx]
                left = i
            



if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    sol.trap()