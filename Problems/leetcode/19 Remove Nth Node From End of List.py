class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeList = []
        temp = head
        while head != None:
            nodeList.append(head)
            head = head.next
        if n < len(nodeList):
            node = nodeList[len(nodeList) - n - 1]
            if n > 1:
                node.next = nodeList[len(nodeList) - n + 1]
            else:
                node.next = None
            return temp
        else:
            return temp.next
