# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# need 3 variables: 
#   prev, curr, and temp 
#   curr holds the current node that we are changing the pointer of 
#   prev holds the last node just changed
#   temp holds the curr.next so we don't lose the chain
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
