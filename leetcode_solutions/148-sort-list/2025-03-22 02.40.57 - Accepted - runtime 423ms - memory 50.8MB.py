# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case：空 or 只有一個節點時，直接返回
        if not head or not head.next:
            return head

        # Step 1: 使用快慢指針找到中點
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: 將鏈結串列從中間切兩半
        mid = slow.next
        slow.next = None  # 斷開鏈結

        # Step 3: 對左右兩半遞迴排序
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 4: 合併兩個排序後的鏈表
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # 接上剩下的節點
        tail.next = l1 if l1 else l2

        return dummy.next
        