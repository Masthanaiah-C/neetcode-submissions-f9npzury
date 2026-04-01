# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Condition
        if (head == None or head.next == None):
            return head
        # iniitalisation
        prevNode = head
        currNode = head.next
        nextNode = currNode.next
        # reverse the links
        while (currNode != None):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            

        head.next = None
        return prevNode 