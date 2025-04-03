# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergesort(self, left , right):
        Dummy = ListNode()
        curr = Dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        return Dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_node = slow.next
        slow.next = None

        left , right = self.sortList(head), self.sortList(mid_node)


        return self.mergesort(left,right)

