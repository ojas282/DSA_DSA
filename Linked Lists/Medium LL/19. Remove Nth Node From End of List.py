# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_len(self,head):
        if head is None:
            return 0
        if head.next is None:
            return 1
        curr = head
        count = 1
        while curr and curr.next:
            count += 1
            curr = curr.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_to_traverse = self.find_len(head) - n
        if len_to_traverse == 0 :
            #remove first node
            curr = head.next
            head = curr
            return head
        if len_to_traverse > 0:
            curr = head
            len_to_traverse -= 1
            while len_to_traverse != 0:
                curr = curr.next
                len_to_traverse -= 1
            c = curr.next
            curr.next = c.next
            return head
            


