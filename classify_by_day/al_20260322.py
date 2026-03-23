from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## First Approach
        # temp = []
        # cri = (len(nums1) + len(nums2)) / 2
        # cur = 0
        #
        # idx1, idx2 = 0, 0
        # while cur <= cri:
        #     if idx1 < len(nums1) and idx2 < len(nums2):
        #         if nums1[idx1] <= nums2[idx2]:
        #             temp.append(nums1[idx1])
        #             idx1 += 1
        #         else:
        #             temp.append(nums2[idx2])
        #             idx2 += 1
        #     elif idx1 < len(nums1):
        #         temp.append(nums1[idx1])
        #         idx1 += 1
        #     elif idx2 < len(nums2):
        #         temp.append(nums2[idx2])
        #         idx2 += 1
        #     cur += 1
        #
        # if cri % 1 == 0:
        #     return (temp[-1] + temp[-2]) / 2
        # else:
        #     return temp[-1]

        ## Second Approach
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2
            else:
                return nums2[len(nums2) // 2]
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
            else:
                return nums1[len(nums1) // 2]
        small, big = nums1, nums2
        if len(nums1) > len(nums2):
            small, big = nums2, nums1

        half = (len(nums1) + len(nums2)) // 2

        small_left, small_right = 0, len(small) - 1

        while small_left <= small_right:
            mid = (small_left + small_right) // 2
            mid_big = half - (mid + 1)
            print(half, mid, mid_big, small, big)
            if small[mid] > big[mid_big]:
                if mid_big + 1 < len(big) and big[mid_big + 1] < small[mid]:
                    small_right = mid - 1
                else:
                    if (len(nums1) + len(nums2)) % 2 == 0:
                        if mid > 0:
                            return (max(small[mid - 1], big[mid_big]) + small[mid]) / 2
                        else:
                            return (big[mid_big] + small[mid]) / 2
                    else:
                        return small[mid]
            elif small[mid] < big[mid_big]:
                if mid + 1 < len(small) and small[mid + 1] < big[mid_big]:
                    small_left = mid + 1
                else:
                    if (len(nums1) + len(nums2)) % 2 == 0:
                        if mid_big > 0:
                            return (max(small[mid], big[mid_big - 1]) + big[mid_big]) / 2
                        else:
                            return (small[mid] + big[mid_big]) / 2
                    else:
                        return big[mid_big]
            else:
                return small[mid]
        if small_right <0:
            return big[half]
        else:
            return big[half-len(small)]



nums1 = [-10, -9, -8]
nums2 = [1, 2]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))





