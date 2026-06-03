# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # # CONVERT TO ARRAY METHOD
        # curr = head
        # arr = []
        # while curr:
        #     arr.append(curr)
        #     curr = curr.next
        # return arr[len(arr) // 2]

        # TWO-POINTER (SLOW/FAST)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow