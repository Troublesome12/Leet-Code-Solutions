# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        head_list.pop(len(head_list) - n)
        
        if len(head_list) == 0:
            return None

        new_head = ListNode(head_list.pop())
        for i in range(len(head_list)-1, -1, -1):
            head = ListNode(head_list[i], new_head)
            new_head = head
            
        return new_head
            
        