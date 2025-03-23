class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Step 1: 用普通 dict 建圖
        graph = {}
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            # 確保 b 在 graph 中已初始化
            if b not in graph:
                graph[b] = []
            graph[b].append(a)

            # a 的入度 +1
            in_degree[a] += 1

        # Step 2: 將所有入度為 0 的課程放進 queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        # Step 3: 拓撲排序
        while queue:
            course = queue.popleft()
            completed += 1

            # 如果 course 沒有任何後繼節點，跳過
            if course not in graph:
                continue

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: 是否完成所有課程
        return completed == numCourses
        