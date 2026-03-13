class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        memory = {"a": -1, "b": -1, "c": -1}
        for idx, c in enumerate(s):
            memory[c] = idx

            if memory["a"] != -1 and memory["b"] != -1 and memory["c"] != -1:
                start = min(memory.values())
                answer += start + 1

        return answer


explain = """If we fix the end of the string as the current index in the for-loop, 
we can count the number of valid substrings only once with length (current_index + 1 + alpha).

Here, alpha is determined by the minimum value in the memory 
that records the most recent index of each character.
"""