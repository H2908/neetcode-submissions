"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        # Step1 : Insert copy node after every original node
        curr = head

        while curr:
            copy = Node(curr.val)

            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step : Copy the random Pointer
        curr = head

        while curr:
            if curr.random:
                cuur.next.random = curr.random.next

            curr = curr.next.next

        # Step3 Seperate the 2 lists
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copy_head
