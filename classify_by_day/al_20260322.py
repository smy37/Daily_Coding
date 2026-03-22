from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        cri = (len(nums1) + len(nums2)) / 2
        cur = 0

        idx1, idx2 = 0, 0
        while cur <= cri:
            if idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1] <= nums2[idx2]:
                    temp.append(nums1[idx1])
                    idx1 += 1
                else:
                    temp.append(nums2[idx2])
                    idx2 += 1
            elif idx1 < len(nums1):
                temp.append(nums1[idx1])
                idx1 += 1
            elif idx2 < len(nums2):
                temp.append(nums2[idx2])
                idx2 += 1
            cur += 1

        if cri % 1 == 0:
            return (temp[-1] + temp[-2]) / 2
        else:
            return temp[-1]