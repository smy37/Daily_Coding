from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cur = students[:]

        student = deque(students)
        sand = deque(sandwiches)

        while student:
            if student[0] == sand[0]:
                student.popleft()
                sand.popleft()
            else:
                cur = list(student)[:]
                s = student.popleft()
                student.append(s)

            if cur == list(student):
                break

        return len(student)


students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
sol = Solution()
print(sol.countStudents(students, sandwiches))