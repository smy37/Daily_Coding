from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        last_dict = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_dict:
                last_dict[s[i]] = i

        cur_group = 0
        group_start = 0
        for i in range(len(s)):
            cur_group = max(cur_group, last_dict[s[i]])

            if i == cur_group:

                answer.append(cur_group-group_start+1)
                group_start = cur_group+1
        return answer

if __name__ == "__main__":
    t_s = "eccbbbbdec"
    sol = Solution()
    print(sol.partitionLabels(t_s))

    explain = """
    First, construct a dictionary that stores the last index of each character.  
    Then, form groups by splitting whenever the current index reaches the last index of the group.
    """