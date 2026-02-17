import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## First Approach
        # target = {s: 0 for s in string.ascii_lowercase}
        # for s in s1:
        #     target[s] += 1

        # for i in range(len(s2)):
        #     if target[s2[i]] >= 1:
        #         temp = {s: 0 for s in string.ascii_lowercase}
        #         for j in range(i, len(s2)):
        #             temp_s = s2[j]
        #             if temp_s not in target or temp[temp_s] +1 > target[temp_s]:
        #                 break
        #             temp[temp_s] += 1
        #
        #             if temp == target:
        #                 return True

        ## Second Approach
        target = {s: 0 for s in string.ascii_lowercase}
        for s in s1:
            target[s] += 1

        left_idx, right_idx = 0, 0
        temp = {s: 0 for s in string.ascii_lowercase}
        while left_idx <= right_idx and right_idx < len(s2):
            right_s = s2[right_idx]
            if target[right_s] == 0:
                temp = {s: 0 for s in string.ascii_lowercase}
                right_idx += 1
                left_idx = right_idx
                continue
            elif temp[right_s] + 1 > target[right_s] :
                while temp[right_s] >= target[right_s] :
                    left_s = s2[left_idx]
                    temp[left_s] -= 1
                    left_idx += 1
            temp[right_s] += 1
            right_idx += 1
            if temp == target:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))