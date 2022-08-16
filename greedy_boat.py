from collections import deque


people = [70, 80, 50]
limit = 100

def solution(people, limit):
    people = sorted(people)
    people = deque(people)
    answer = 0
    while len(people)>1:
        cur = people.pop()
        if cur + people[0] <= limit:
            answer +=1
            people.popleft()
        else:
            answer +=1
    if len(people) ==1:
        answer +=1
    return answer


print(solution(people, limit))