from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hash = {}
        for s in strs:
            sort_s = tuple(sorted(s))

            if sort_s not in str_hash:
                str_hash[sort_s] = []
            str_hash[sort_s].append(s)
        answer = []
        for k in str_hash:
            answer.append(str_hash[k])

        return answer


if __name__ == "__main__":
    test_case = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    print(sol.groupAnagrams(test_case))

    explain = """
    By sorting the string and using the sorted result as a dictionary key, 
    we can group or identify equivalent strings efficiently.
    """