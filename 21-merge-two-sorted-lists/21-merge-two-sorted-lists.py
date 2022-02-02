# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        myList = []
        if list1:
            while True:
                myList.append(list1.val)
                if list1.next is None:
                    break
                list1 = list1.next
        
        if list2:
            while True:
                myList.append(list2.val)
                if list2.next is None:
                    break
                list2 = list2.next
        
        myList.sort()
        myList.reverse()
        if not len(myList):
            return None
        
        ln = ListNode(myList[0])
        
        for i in range(1, len(myList)):
            ln = ListNode(myList[i], ln)
            
        return ln
        