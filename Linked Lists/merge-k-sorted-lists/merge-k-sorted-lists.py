import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Can use a min-heap to keep tracking of our current min.
        # Add all nodes and their values to the heap, and start popping off a value and node.
        # Build return list based off this order.
        node_heap = [(node.val, index) for index, node in enumerate(lists) if node]
        heapq.heapify(node_heap)
        print(lists)
        
        merged_list = current = ListNode(None)
        while node_heap:
            value, index = heapq.heappop(node_heap)
            current.next = ListNode(value)
            current = current.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(node_heap, (lists[index].val, index))
        return merged_list.next