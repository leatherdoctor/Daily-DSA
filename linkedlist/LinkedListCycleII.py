class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head):
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return current
            
            visited.add(current)
            current = current.next
        
        return None


# ----- Creating Linked List -----
# 3 -> 2 -> 0 -> -4
#      ^         |
#      |_________|

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2   # cycle starts at node2

head = node1


# ----- Running the Solution -----
sol = Solution()
cycle_node = sol.detectCycle(head)

if cycle_node:
    print("Cycle starts at node with value:", cycle_node.val)
else:
    print("No cycle detected")