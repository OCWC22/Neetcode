
#Leetcode 148
#https://leetcode.com/problems/sort-list/


#https://www.youtube.com/watch?v=TGveA1oFhrc

# Merge Sort
# Time Complexity: O(nlogn)
# Space Complexity: log(n) because using recursion, O(1) Would Take too long

#           4 -> 2 -> 1 -> 3
#      4 -> 2           -> 1 -> 3
#    4      -> 2      -> 1      -> 3      log(n), bc # of times divide n by 2 to get to each node is separated

#      2 -> 4           -> 1 -> 3         O(n), bc merging 2 sorted lists
#           1 -> 2 -> 3 -> 4

# Total Time Complexity: O(nlogn)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    #push values into linked list
    def append(self, value):
        #init new node
        new = Node(value)

        if self.head is None:
            self.head = new
            return        
        curr = self.head
        while curr.next:
            curr = curr.next
        #append new node at end of linked list
        curr.next = new 
                
    def merge(self, l1, l2):
        result = None

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.data <= l2.data:
            result = l1 
            result.next = self.merge(l1.next, l2)
        else:
            result = l2
            result.next = self.merge(l1, l2.next)
        return result

        

    def sortList(self, head):
        
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMid(self, head):
        #slow/fast pointers

        if (head == None):
            return head

        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def printList(head):
    if head is None:
        print(' ')
        return
    curr = head
    while curr:
        print(curr.data, end = " ")
        curr = curr.next
    print(' ')


if __name__ == '__main__':
    l = LinkedList()

    l.append(4)
    l.append(2)
    l.append(1)
    l.append(3)

    l.head = l.sortList(l.head)
    print("Sorted Linked List: " )
    printList(l.head)

