class Solution:
    '''
    計算 2D 二元地圖 grid 中的 島嶼數量。
    '1' 代表陸地，'0' 代表水域。
    島嶼 是由 相鄰的陸地（水平或垂直連接）組成的區塊。
    島嶼必須完全被水包圍，地圖邊界也視為水域。

    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            """ 深度優先搜尋（DFS）探索並標記島嶼 """
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return  # 出界或遇到水，直接返回
            grid[r][c] = "0"  # 標記已訪問
            # 向四個方向擴展
            dfs(r + 1, c)  # 向下
            dfs(r - 1, c)  # 向上
            dfs(r, c + 1)  # 向右
            dfs(r, c - 1)  # 向左

        # 遍歷 grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # 發現新島嶼
                    island_count += 1
                    dfs(r, c)  # 用 DFS 標記整座島嶼

        return island_count
        