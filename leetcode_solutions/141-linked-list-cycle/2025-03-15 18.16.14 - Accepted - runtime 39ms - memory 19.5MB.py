# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head  # 初始化快慢指針
        
        while fast and fast.next:  # 當 fast 沒有到達鏈結串列尾部
            slow = slow.next  # slow 移動一步
            fast = fast.next.next  # fast 移動兩步
            
            if slow == fast:  # 如果相遇，代表有環
                return True

        return False  # 如果 fast 到達 None，代表無環

# 測試函數
def createLinkedListWithCycle(values, pos):
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]  # 創建環
    
    return nodes[0] if nodes else None