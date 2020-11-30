class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def addTwoHugeNumbers(a, b):

    # put value of a into s1
    c = a
    s1 = ""
    while c:
        c.value = str(c.value)
        while len(c.value) < 4:
            c.value="0"+c.value            
        s1 += c.value
        c = c.next
        
    # put value of b onto s2
    c = b
    s2 = ""
    while c:
        c.value = str(c.value)
        while len(c.value) < 4:
            c.value = "0" + c.value            
        
        s2 += c.value
        c = c.next
        
    output = str(int(s1)+int(s2))
    
    linkedOutput=[0]
    linkedOutput[0]=""
    
    for i in range(len(output)-1, -1, -1):
        if len(linkedOutput[0])==4:
            linkedOutput[0] = int(linkedOutput[0])
            linkedOutput.insert(0, "")

        linkedOutput[0] = output[i] + linkedOutput[0]
        
    linkedOutput[0]=int(linkedOutput[0])
    
    return linkedOutput

#
def addTwoHugeNumbers2(a, b):
    a = reverse(a)
    b = reverse(b)
    
    carry = 0
    result = None
    
    while a is not None or b is not None or carry > 0:
        raw = ((a.value if a is not None else 0) + 
               (b.value if b is not None else 0) + 
               carry)
                
        node = ListNode(raw % 10000)
        node.next = result
        
        result = node
        carry = raw // 10000
        
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next
            
    return result
    
def reverse(list):
    current = list
    previous = None
    
    while current is not None:
        previous, current.next, current = current, previous, current.next
        
    return previous
    
def listToLinkedList(lst):
    ll = ListNode(lst[0])
    for i in lst[1:]:
        ptr = ll
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(i)
    return ll

def main():
    a = listToLinkedList([9876, 5432, 1999])
    b = listToLinkedList([1, 8001])

    print(addTwoHugeNumbers(a,b))
    
    a = listToLinkedList([123, 4, 5])
    b = listToLinkedList([100, 100, 100])
    result = addTwoHugeNumbers2(a,b)
    while result:
        print(f"{result.value}",end=" ")
        result = result.next

   

if __name__ == "__main__":
    main()