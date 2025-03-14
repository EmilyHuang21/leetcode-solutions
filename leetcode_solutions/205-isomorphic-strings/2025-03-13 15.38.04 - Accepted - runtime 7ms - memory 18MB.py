class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # 長度必須相同，否則直接返回 False

        s_to_t = {}  # 記錄 s -> t 的對應關係
        t_to_s = {}  # 記錄 t -> s 的對應關係

        for char_s, char_t in zip(s, t):
            # 檢查是否已經有對應關係，且對應字母一致
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False  # 發現矛盾，返回 False
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False  # 發現矛盾，返回 False

            # 建立映射關係
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True