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