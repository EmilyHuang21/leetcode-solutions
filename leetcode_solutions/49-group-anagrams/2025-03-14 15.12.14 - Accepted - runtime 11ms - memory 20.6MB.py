class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}  # 用字典來儲存異位詞群組
        for word in strs:
            key = "".join(sorted(word))  # 將字母排序後作為 Key
            if key not in anagrams:
                anagrams[key] = []  # 若 Key 不存在，則初始化
            anagrams[key].append(word)  # 將單詞加入對應的群組

        return list(anagrams.values())  # 返回所有異位詞群組