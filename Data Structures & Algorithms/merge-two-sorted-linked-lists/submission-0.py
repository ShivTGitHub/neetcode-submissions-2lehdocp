# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(-1)
        curr=head
        temp1=list1
        temp2=list2
        while(temp1 and temp2):
            if(temp1.val<=temp2.val):
                curr.next=ListNode(val=temp1.val)
                temp1=temp1.next
            else:
                curr.next=ListNode(val=temp2.val)
                temp2=temp2.next
            curr=curr.next
        while(temp1):
            curr.next=ListNode(temp1.val)
            curr=curr.next
            temp1=temp1.next
        while(temp2):
            curr.next=ListNode(temp2.val)
            curr=curr.next
            temp2=temp2.next

        return head.next