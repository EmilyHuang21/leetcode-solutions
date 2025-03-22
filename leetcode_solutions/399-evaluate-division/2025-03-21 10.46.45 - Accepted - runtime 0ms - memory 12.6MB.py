class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)

        # 建圖：每個除法建立雙向關係
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                res = dfs(neighbor, end, visited)
                if res != -1.0:
                    return graph[start][neighbor] * res
            return -1.0

        # 執行每筆查詢
        return [dfs(a, b, set()) for a, b in queries]