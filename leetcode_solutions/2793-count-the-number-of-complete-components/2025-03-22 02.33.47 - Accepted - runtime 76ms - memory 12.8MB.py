class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int                      # 節點數（從 0 到 n-1）
        :type edges: List[List[int]]     # 邊的列表，每個邊是 [a, b]
        :rtype: int                      # 回傳完全圖元件的數量
        """

        # Step 1: 建立無向圖的鄰接表
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: 初始化 visited 陣列
        visited = [False] * n
        count = 0  # 用來統計完全圖的數量

        # Step 3: DFS 搜索一整個連通元件
        def dfs(node, nodes, edge_count):
            visited[node] = True      # 標記目前節點已走訪
            nodes.append(node)        # 收集這個元件的節點
            for nei in graph[node]:   # 拜訪所有鄰居
                edge_count[0] += 1    # 每遇到一條邊就 +1（注意：會重複記錄）
                if not visited[nei]:
                    dfs(nei, nodes, edge_count)

        # Step 4: 遍歷所有節點
        for i in range(n):
            if not visited[i]:
                nodes = []           # 收集此元件中的所有節點
                edge_count = [0]     # 使用 list 包起來方便在 DFS 中修改

                dfs(i, nodes, edge_count)  # 搜索這個元件

                v = len(nodes)             # 元件內節點數
                e = edge_count[0] // 2     # 因為是無向圖，每條邊被計算兩次 → 除以 2

                # Step 5: 檢查是否是完全圖
                # 完全圖的邊數應為 v * (v - 1) / 2
                if e == v * (v - 1) // 2:
                    count += 1

        return count
        