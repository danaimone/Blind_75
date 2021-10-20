# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Set a current pointer to the head, and the previous pointer to none.
            While we still have a next pointer for our current node,
            create a temporary node for the current node's next. The current nodes next
            node will become the previous, previous will become the current, and current
            will become the next node (that we stored in temp_next)
            Previous points to head of reversed linked list
        '''
        current = head
        previous = None
        while current:
            temp_next = current.next
            current.next = previous
            previous = current
            current = temp_next
        return previous
        