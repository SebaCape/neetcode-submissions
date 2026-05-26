class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        #Create indegree array for Kahn's algorithm
        indegree = [0] * num_courses
        req_map = defaultdict(list)

        #Populate prerequisite dictionary and evaluate indegrees
        for course, req in prerequisites:
            indegree[req] += 1
            req_map[course].append(req)

        #Initialize queue with all valid initial nodes
        q = deque([_ for _ in range(num_courses) if indegree[_] == 0])

        res, end_course = [], 0

        #Indegree guided BFS
        while q:
            cur =  q.popleft()
            res.append(cur)
            end_course += 1
            #Subtract from indegrees until valid (activates next level of courses)
            for req in req_map[cur]:
                indegree[req] -= 1
                if indegree[req] == 0:
                    q.append(req)

        #Return empty array if there exists some course impossible to qualify for, otherwise return topologically sorted ordering
        if end_course != num_courses:
            return []

        return res[::-1]