# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or a single node
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        middle = self.find_middle(head)
        print(f'middle: {middle}')
        # Split the linked list into two halves
        left_half = head
        print(f'left half: {left_half}')
        right_half = middle.next
        print(f'right half: {right_half}')
        middle.next = None
        print(f'left half after middle.next = None: {left_half}')
        print(f'right half after middle.next = None: {right_half}')
        # Recursively sort the two halves
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)

        # Merge the sorted halves
        sorted_list = self.merge(left_sorted, right_sorted)

        return sorted_list

    def find_middle(self, head: ListNode) -> ListNode:
        # Use two pointers to find the middle of the linked list
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        # Merge two sorted linked lists
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # If one of the lists is not empty, append the remaining nodes
        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next