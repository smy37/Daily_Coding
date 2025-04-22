### 다른 사람 풀이 많이 참고하였음 잊어 먹을때 쯤 곱씹어서 다시 풀어보기.....
def solution(arrows):
    answer = 0
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    x = 0
    y = 0
    visited = {}
    visited[(0,0)] = []
    for dir in arrows:
        for _ in range(2):
            n_x = x + dx[dir]
            n_y = y + dy[dir]
            if (n_x,n_y) in visited and (x,y) not in visited[(n_x,n_y)]:
                visited[(n_x,n_y)].append((x,y))
                if(x,y) not in visited:
                    visited[(x,y)] = []
                visited[(x,y)].append((n_x,n_y))
                answer +=1
            elif (n_x,n_y) not in visited:
                visited[(n_x,n_y)] = []
                visited[(n_x,n_y)].append((x,y))
                visited[(x,y)].append((n_x,n_y))
            x = n_x
            y = n_y


    return answer


if __name__ == "__main__":
    print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]),3)
    print(solution([5, 2, 7, 1, 6, 3]), 3)
    print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0] ), 3)