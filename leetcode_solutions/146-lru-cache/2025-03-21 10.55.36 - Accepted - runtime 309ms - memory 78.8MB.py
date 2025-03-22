from collections import defaultdict

# 雙向鏈結串列節點
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}           # key -> 節點
        self.capacity = capacity
        self.size = 0

        # 初始化虛擬頭尾節點（方便操作）
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 將新節點加到最前面
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    # 將節點從鏈結串列中移除
    def _remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # 將節點移到最前面（代表最近使用）
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    # 移除最後一個節點（最少使用）
    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        # 每次 get 都算使用，要移到最前面
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            # 新節點
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1

            if self.size > self.capacity:
                # 超出容量，移除最久沒使用的
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # 如果 key 已存在，更新值，並移到最前面
            node.value = value
            self._move_to_head(node)
