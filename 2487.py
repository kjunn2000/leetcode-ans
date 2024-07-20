from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dq = deque()
        temp = head
        while temp != None: 
            while len(dq) != 0 and dq[-1] < temp.val:
                dq.pop()
            dq.append(temp.val)
            temp = temp.next
        temp = ListNode()
        newHead = temp
        while len(dq) != 0:
            temp.next = ListNode(dq.popleft())
            temp = temp.next
        return newHead.next 
            
        

        