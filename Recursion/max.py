import sys

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
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
        
    def largest(self):
        return r_largest(self.head)
        
def r_largest(ptr, largest = -100000):
    if ptr == None:
        return largest
    elif int(ptr.item) > largest:
        largest = int(ptr.item)
        return r_largest(ptr.next, largest)
    else:
        return r_largest(ptr.next, largest)

def main():
    
    # Read each set
    line = '-14 7495 -237 294 -5893 -285 7421 -921 1441'
    items = line.strip().split()
    nums = [int(item) for item in items] # Create an array of nums from the strings
    
    ll = LinkedList()

    # Add each number to the list
    for num in nums:
        ll.add(num)
    
    # call the students function
    print("Using largest function, {}".format(ll.largest()))

    print("Using the built-in max function, {}".format(max(nums)))

if __name__ == "__main__":
main()
