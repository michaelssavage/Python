class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def removeKFromList(l,k):
    c = ListNode(None)
    c.next = l
    curr = c
    while curr:
        while curr.next and curr.next.value == k:
            curr.next = curr.next.next
        curr = curr.next
    return c.next

def removeKFromList2(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l


l = ListNode([3, 1, 2, 3, 4, 5])
k = 3
print(removeKFromList2(l,k).value)

