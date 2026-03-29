class Solution:
    def mergeKLists(self, lists: List[ListNode]):
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        curr = res
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next

        return res.next
        