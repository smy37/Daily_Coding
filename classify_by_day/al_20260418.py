class Solution:
    def reverse(self, x: int) -> int:
        cri = 2 ** 31
        if -cri > x or x > cri - 1:
            return 0
        x = str(x)[::-1]
        if x[-1] == "-":
            x = -int(x[:-1])
        else:
            x = int(x)

        if -cri > x or x > cri - 1:
            return 0
        else:
            return x


if __name__ == "__main__":
    test_case = -123
    sol = Solution()
    print(sol.reverse(test_case))

    explain = """32-bit int's range is [-2**31, 2**31-1] since number of this range is (2**31-1-(-2**31)+1) = 2**32.
    """