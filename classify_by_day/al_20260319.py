from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left = 0
        temp_list = []

        for right, h in enumerate(height):
            if height[left] < h:
                cri = height[left]
                ori_right = right

                while temp_list and cri > temp_list[-1][1]:
                    last_idx, last_h = temp_list.pop()
                    answer += (right - last_idx) * (cri - last_h)
                    right = last_idx
                left = ori_right
                temp_list = [[ori_right, h]]
            else:
                cri = h
                last_idx = right
                while temp_list and cri >= temp_list[-1][1]:
                    last_idx, last_h = temp_list.pop()
                    answer += (right-last_idx)*(cri-last_h)
                    right = last_idx

                temp_list.append([last_idx, cri])

        return answer


if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    sol = Solution()
    print(sol.trap(height))