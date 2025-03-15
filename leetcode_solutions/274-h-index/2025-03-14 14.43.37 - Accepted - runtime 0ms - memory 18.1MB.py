class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # 步驟 1：將引用數降序排序
        h = 0  # 初始化 h-index

        for i, citation in enumerate(citations):
            if citation >= i + 1:  # 步驟 2：檢查是否至少有 h 篇論文的引用數 ≥ h
                h = i + 1
            else:
                break  # 若條件不滿足則終止

        return h
