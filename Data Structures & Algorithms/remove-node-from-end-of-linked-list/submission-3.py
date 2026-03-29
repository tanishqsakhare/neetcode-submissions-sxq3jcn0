class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head