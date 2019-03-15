import sys

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
        
    def count(self):
        return r_count(self.head)         #this method will start the recursive method

def r_count(ptr):
    if ptr == None:
        return 0
    else:
        return r_count(ptr.next) + 1

def main():
    # Read each set
    line = sys.stdin.readline()           #Enter from command line
    items = line.strip().split()
    
    ll = LinkedList()
    # call the students function
    print(ll.count())                     # Empty list, count should return 0
    
    for item in items:
        ll.add(item)
    
    # call the students function
    print(ll.count())
    
    # check that the first item removed from the list is the same as the last one added
    same = ll.remove() == items.pop()
    
    # call the students function again ... should be one shorter.
    print(ll.count())
    
    while not ll.is_empty() and len(items) > 0:
        same = same and ll.remove() == items.pop()
        
    if not same or not ll.is_empty() or len(items) != 0:
        print("the list has been modified!");

if __name__ == "__main__":
main()
