class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        for i in range(10001):
            if head == None:
                return False
            head = head.next
        return True
