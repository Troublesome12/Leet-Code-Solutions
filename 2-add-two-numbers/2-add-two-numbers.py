# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def convert_to_linked_list(self, my_list: list[int]) -> Optional[ListNode]:
        count = 0
        for value in my_list:
            if count == 0:
                node = ListNode(value, None)
            else:
                node = ListNode(value, node)
            
            count += 1

        return node
    
    def convert_to_list(self, list_node: Optional[ListNode]) -> list[int]:
        node = list_node
        a = []
        while node is not None:
            a.append(node.val)
            node = node.next
            
        return a
    
    def list_to_int(self, integers: list[int]) -> int:
        strings = [str(integer) for integer in integers]
        a_string = "".join(strings)
        return int(a_string)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a = self.convert_to_list(l1)
        b = self.convert_to_list(l2)
        
        a.reverse()
        b.reverse()
        
        a = self.list_to_int(a)
        b = self.list_to_int(b)
        result = a + b
        
        result = [int(x) for x in str(result)]
        
        l3 = self.convert_to_linked_list(result)
        
        return l3