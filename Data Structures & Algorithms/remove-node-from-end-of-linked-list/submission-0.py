# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head):
        prev=None
        curr=head

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        return prev    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # step 1 Reverse the linked list
        head=self.reverse(head)

        #step2 Remove nth node from the beginning

        if n==1:
            head=head.next
        else:
            curr=head

            for _ in range(n-2):
                curr=curr.next

            curr.next=curr.next.next

        # step 3: Reverse again
        head=self.reverse(head)

        return head            
        