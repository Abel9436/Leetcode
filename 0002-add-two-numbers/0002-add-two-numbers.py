# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def add(node1, node2, carry):
            if not node1 and not node2 and carry == 0:
                return None
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            total = val1 + val2 + carry
            new_carry = total // 10
            digit = total % 10
            current_node = ListNode(digit)
            current_node.next = add(
                node1.next if node1 else None,
                node2.next if node2 else None,
                new_carry
            )
            return current_node
        
        return add(l1, l2, 0)
