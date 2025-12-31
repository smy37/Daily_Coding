from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # right_idx = len(height) // 2
        # left_idx = right_idx - 1
        # answer = (right_idx-left_idx)*min(height[right_idx], height[left_idx])

        ## First Approach
        # max_right, max_left = right_idx, left_idx
        # max_right_value, max_left_value = 0, 0

        # for i in range(right_idx, len(height)):
        #     if (i - left_idx) * height[i] > max_right_value:
        #         max_right_value = (i + 1) * height[i]
        #         max_right = i
        #
        # for i in range(left_idx, -1, -1):
        #     if (right_idx - i) * height[i] > max_left_value:
        #         max_left_value = (i + 1) * height[i]
        #         max_left = i
        # print(max_left, max_right)
        # answer = (max_right - max_left) * min(height[max_left], height[max_right])

        ## Second Approach
        # while (right_idx < len(height)-1 or left_idx >0):
        #     print(left_idx, right_idx)
        #     if left_idx == 0:
        #         if right_idx < len(height)-1:
        #             right_idx += 1
        #     elif right_idx == len(height)-1:
        #         if left_idx > 0:
        #             left_idx -= 1
        #     else:
        #         if height[left_idx] <= height[right_idx]:
        #             right_idx += 1
        #         else:
        #             left_idx -= 1
        #     answer = max(answer, (right_idx-left_idx)*min(height[right_idx], height[left_idx]))

        ## Third Approach
        left_idx, right_idx = 0, len(height)-1
        answer = 0

        while left_idx < right_idx:
            answer = max(answer, (right_idx-left_idx)*min(height[right_idx], height[left_idx]))

            if height[left_idx] <= height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1

        return answer

if __name__ == "__main__":
    # test_case = [1, 2, 4, 3]
    test_case = [4,3,2,1,4]
    sol = Solution()
    print(sol.maxArea(test_case))

    explain = """
    The most important point is that the two pointers start at both ends.
    """
