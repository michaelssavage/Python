class ListNode(object):
    def __init__(self, x, next=None):
        self.value = x
        self.next = next

def isListPalindrome(l):
    if not l or not l.next:
        return True
    s = 1
    n = l
    while n.next:
        n = n.next
        s += 1

    middle = s // 2

    n = l
    for i in range(middle):
        n = n.next

    if s % 2:
        n = n.next

    r = n # reverse n
    m = r.next
    for _ in range(middle-1): # flip n
        m.next,r,m = r,m,m.next

    for _ in range(middle):
        if r.value != l.value:
            return False
        r = r.next
        l = l.next

    return True

def main():
    nums = [1,2,3,2,1]

    # add numbers to listNode
    lst = ListNode(nums[0])
    for i in nums[1:]:
        ptr = lst
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(i)

    print(isListPalindrome(lst))
   

if __name__ == "__main__":
    main()

