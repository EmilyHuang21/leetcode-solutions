class Solution(object):
    '''
     解法步驟：
        對 queries 做排序（記錄原始 index）
        使用 min-heap，從 (0, 0) 出發，所有可拜訪的格子依序加入 heap（根據格子值小到大）
        用 visited 記錄格子是否拜訪過，避免重複計算
        當格子值小於當前 query，就從 heap 中 pop 出來、加入 point 計數，並將周圍 4 格加入 heap
        記錄每個 query 對應的 point 到 result 陣列  
    '''
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        q_idx = sorted([(val, i) for i, val in enumerate(queries)])  # 對 query 排序

        visited = [[False]*n for _ in range(m)]  # 拜訪狀態
        heap = [(grid[0][0], 0, 0)] if grid[0][0] < max(queries) else []  # 小根堆初始
        visited[0][0] = True

        ans = [0]*len(queries)
        count = 0  # 拜訪格子數

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]  # 上下左右方向

        # 當 query 從小到大處理
        for val, idx in q_idx:
            while heap and heap[0][0] < val:
                _, r, c = heapq.heappop(heap)
                count += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            ans[idx] = count  # 該 query 能拜訪的格子數
        return ans
        