"""
Problem: Reverse Linked List
Platform: LeetCode
Difficulty: Easy
Approach: Iterative pointer reversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


# Helper function to print list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Create example linked list: 1 → 2 → 3 → 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original List:")
print_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed List:")
print_list(reversed_head)