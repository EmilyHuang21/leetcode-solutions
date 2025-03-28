class TrieNode(object):
    def __init__(self):
        # children: 字典，key 是字母，value 是 TrieNode
        self.children = {}
        self.is_end = False  # 表示是否為單字結尾


class WordDictionary(object):

    def __init__(self):
        # 建立一個 Trie 的根節點
        self.root = TrieNode()

    def addWord(self, word):
        """
        將一個單字加入到 Trie 樹中
        """
        node = self.root
        for char in word:
            # 如果該字母不存在，先建立對應的 TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # 向下一層移動
            node = node.children[char]
        # 單字結尾標記
        node.is_end = True

    def search(self, word):
        """
        搜尋字典中是否有符合的單字，支援 '.' 模糊匹配
        """

        def dfs(index, node):
            # 若已經走完 word 的每一個字元
            if index == len(word):
                return node.is_end

            char = word[index]

            # 如果當前字元是 '.'，表示可以匹配任意一個子節點
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                # 如果不是 '.'，則需確認該字母是否存在於 children 中
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        # 從 index 0 和 root 開始搜尋
        return dfs(0, self.root)
