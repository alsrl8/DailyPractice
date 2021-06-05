class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        temp = head
        while temp != None:
            temp = temp.next
            cnt += 1
        
        temp = head
        for i in range(cnt//2):
            temp = temp.next
        return temp
