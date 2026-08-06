# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify list Creation
        dummy=ListNode(0)

        # Pointer to build the answer list 
        curr = dummy

        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            # calculate the total
            total=val1+val2+carry
            digit=total%10
            carry=total//10

            curr.next=ListNode(digit)
            curr=curr.next

            #Move L1 if possible
            if l1:
                l1=l1.next

            #Move l2 if possible 
            if l2:
                l2=l2.next

        return dummy.next
                    