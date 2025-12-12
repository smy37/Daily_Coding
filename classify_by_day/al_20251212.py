from typing import List

move_x = [1, -1, 0, 0]
move_y = [0, 0, -1, 1]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def dfs(stack, visit):
            cur_x, cur_y, word_idx = stack.pop()
            if word_idx == len(word)-1:
                return True

            for i in range(4):
                next_x, next_y = cur_x + move_x[i], cur_y + move_y[i]
                if 0<=next_x<n and 0<=next_y<m and (next_x, next_y) not in visit:
                    if board[next_x][next_y] == word[word_idx+1]:
                        visit[(next_x, next_y)] = True
                        flag = dfs(stack + [[next_x, next_y, word_idx+1]], visit)
                        del visit[(next_x, next_y)]
                        if flag:
                            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    s = [[i, j , 0]]
                    v = {(i, j): True}
                    answer = dfs(s, v)
                    if answer:
                        return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    sol = Solution()
    print(sol.exist(board, word))

    explain = """
    Each path requires its own unique visited memory, so the visited state must be reset whenever the path changes.  
    For this reason, BFS is not suitable here, and we must use DFS with backtracking.
    """
