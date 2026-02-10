class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        answer = [0 for _ in range(n)]
        stack = []
        cur = 0
        for log in logs:
            num, cmd_type, time = log.split(":")
            if cmd_type == "start":
                spend_time = int(time) - cur
                if len(stack) > 0:
                    stack_num = int(stack[-1][0])
                    answer[stack_num] += spend_time
                cur = int(time)
                stack.append([num, time])
            elif cmd_type == "end":
                start_num, start_time = stack.pop()
                start_num = int(start_num)
                start_time = int(start_time)

                spend_time = int(time) - cur + 1
                answer[start_num] += spend_time
                cur = int(time) + 1

        return answer
