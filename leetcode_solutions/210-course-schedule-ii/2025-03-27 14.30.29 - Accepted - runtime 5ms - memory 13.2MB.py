class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # 建圖與統計每門課的入度
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        # 將所有入度為 0 的課加入 queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        
        while queue:
            course = queue.popleft()
            res.append(course)
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 如果成功排序完所有課程
        if len(res) == numCourses:
            return res
        else:
            return []