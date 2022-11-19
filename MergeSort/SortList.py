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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SortList:
    def sortList(self, head: ListNode) -> ListNode:
        #recursion base case
        if not head or not head.next:
            return head
        #split the list in 2 halves
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

    def to_linked_list(iterable):
        head = None
        for val in reversed(iterable):
            head = ListNode(val, head)
        return head

 




    