# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # return head
        if(not head.next):
            return 

        r=head
        c=0
        while(c<n and r):
            # print(r.val)
            r=r.next
            c+=1
        
        l=head
        if not r:
            # l.next=l.next.next
            return l.next
        while(r.next):
            r=r.next
            l=l.next
        print(l.val)
        l.next=l.next.next
        return head