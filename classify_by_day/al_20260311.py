class Solution:
    def magicalString(self, n: int) -> int:
        answer = 1
        cur_str = [1]
        cur_state = 2
        left = 0
        right = 1

        while len(cur_str) < n:
            cur_str.append(cur_state)
            if cur_state == 1:
                answer += 1
            right += 1

            if right == n: return answer

            left += 1

            for _ in range(cur_str[left] - 1):
                cur_str.append(cur_state)
                if cur_state == 1:
                    answer += 1
                right += 1
                if right == n: return answer

            if cur_state == 2:
                cur_state = 1
            elif cur_state == 1:
                cur_state = 2

        return answer