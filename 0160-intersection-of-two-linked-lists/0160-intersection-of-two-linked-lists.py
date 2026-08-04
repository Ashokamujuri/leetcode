# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        # Traverse both lists; when a pointer reaches the end, switch to the other list's head.
        # They will meet at the intersection node or both hit None at the same time.
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA