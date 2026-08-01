# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2

        if not list2:
            return list1

        # Ensure list1 starts with the smaller value
        if list1.val>list2.val:
            list1,list2=list2,list1

        head= list1

        while list1 and list2:
            prev = None

            while list1 and list1.val<=list2.val:
                prev=list1
                list1=list1.next


            # Insert current node of list2
            prev.next=list2

            #swap the lists
            list1,list2=list2,list1
        return head                    
        