class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dic = dict()
        while headA != None:
            dic.update({headA:True})
            headA = headA.next
        while headB != None:
            if dic.__contains__(headB):
                return headB
            else:
                headB = headB.next
        return None
