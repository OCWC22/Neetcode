#Leetcode  20#6
#https://leetcode.com/problems/reverse-linked-list/description/

#https://neetcode.io/practice

# 1 -> 2 -> 3- > 4
# 4 -> 3 -> 2 -> 1

class ListNode:
    def __init__(self, val):
        self.val = val


#Iterative
#Time: O(n) n = list length
#Space: O(1)

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
#Recursive
