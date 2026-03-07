class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):

        if not head or not head.next:
            return head

        swapped = True

        while swapped:
            swapped = False
            prev = None
            curr = head

            while curr and curr.next:
                nxt = curr.next

                if curr.val > nxt.val:
                    swapped = True

                    # swap nodes
                    curr.next = nxt.next
                    nxt.next = curr

                    if prev:
                        prev.next = nxt
                    else:
                        head = nxt

                    prev = nxt
                else:
                    prev = curr
                    curr = curr.next

        return head


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Creating linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

print("Original List:")
print_list(head)

sol = Solution()
sorted_head = sol.sortList(head)

print("Sorted List:")
print_list(sorted_head)