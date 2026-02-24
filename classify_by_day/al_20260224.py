class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(2, len(s) + 1):
            if len(s) % i == 0:
                cri = len(s) // i
                if s[:cri] * i == s:
                    return True
        return False


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            temp = s[i:] + s[:i]
            if temp == goal:
                return True

        return False


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        cur = a
        time = 1
        cri = len(b) // len(a)
        while len(cur) <= len(a) * (cri + 2):

            if b in cur:
                return time
            time += 1
            cur = a * time
        return -1


explain = """
Triple string matching problem. Set proper index is most important.
"""