from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        course_dict = defaultdict(list)

        for relation in prerequisites:
            next_course, previous_course = relation[0], relation[1]
            course_dict[previous_course].append(next_course)

        checked = [False for _ in range(numCourses)]
        path = [False for _ in range(numCourses)]
        for current_course in range(numCourses):
            if self.isCyclic(current_course, course_dict, checked, path):
                return False

        return True

    def isCyclic(self, current_course, course_dict, checked, path):

        if checked[current_course]:  # node has already been checked and no cycle could be formed
            return False

        if path[current_course]:  # current course index had a path
            return True

        path[current_course] = True

        is_cycle = False
        for child in course_dict[current_course]:
            is_cycle = self.isCyclic(child, course_dict, checked, path)
            if is_cycle:
                break

        path[current_course] = False

        checked[current_course] = True
        return is_cycle