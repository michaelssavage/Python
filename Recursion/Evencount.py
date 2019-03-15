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
    
    def count_even(self):
        return r_count_even(self.head)

def r_count_even(ptr):
    if ptr == None:
        return 0
    elif int(ptr.item) % 2 == 0:
        return r_count_even(ptr.next) + 1
    else:
        return r_count_even(ptr.next)

def main():
    
    line = sys.stdin.readline()                 #Enter from command line
    items = line.strip().split()
    
    ll = LinkedList()
    
    for item in items:
        ll.add(item)

    print("There are {} even numbers.".format(ll.count_even()))

    #while not ll.is_empty():
    #   print(ll.remove())

if __name__ == "__main__":
main()
