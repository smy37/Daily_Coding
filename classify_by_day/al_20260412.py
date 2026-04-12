class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = [[] for _ in range(numRows)]
        mid_num = max(0, numRows-2)
        cri = numRows + mid_num

        for i in range(len(s)):
            cur_idx = i%cri

            if cur_idx >= numRows:
                temp = cur_idx-numRows+1
                answer[-1-temp].append(s[i])
            else:
                answer[cur_idx].append(s[i])

        answer_l = []
        for row in answer:
            for c in row:
                answer_l.append(c)
        return "".join(answer_l)