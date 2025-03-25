from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)  # 為了 O(1) 查找
        if endWord not in wordSet:
            return 0  # 無法達到

        queue = deque()
        queue.append((beginWord, 1))  # (目前的單字, 目前步數)

        while queue:
            word, steps = queue.popleft()
            
            # 嘗試改變 word 中的每個字母
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    next_word = word[:i] + c + word[i+1:]
                    if next_word == endWord:
                        return steps + 1
                    if next_word in wordSet:
                        queue.append((next_word, steps + 1))
                        wordSet.remove(next_word)  # 避免重複使用

        return 0  # 找不到路徑
        