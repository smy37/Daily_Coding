class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        answer = [0 for _ in range(n)]
        stack = []
        cur = 0
        for log in logs:
            num, cmd_type, time = log.split(":")
            if cmd_type == "start":
                if len(stack) > 0:
                    cur - int(stack[-1][1])
                stack.append([num, time])
            elif cmd_type == "end":
                start_num, start_time = stack.pop()
                start_num = int(start_num)
                start_time = int(start_time)

                expend_time = int(time) - start_time + 1
                answer[start_num] = expend_time

        return answer
