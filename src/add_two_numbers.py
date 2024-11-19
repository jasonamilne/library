from typing import Optional, List
from structs.ListNode import ListNode

class Solution():
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        @Description:
        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum of the linked list.

        @Pseudocode:
        -

        @Applications:
        

        @Complexity:
        - Time: O(n)
        - Space: O(n)
        - Algorithm: Linked List

        @Constraints:
        - The number of nodes in each linked list is in the range [1, 100].
        - 0 <= Node.val <= 9
        - It is guaranteed that the list represents a number that does not have leading zeros.

        @Parameters:
        - l1: Optional[ListNode]
        - l2: Optional[ListNode]

        @Returns:
        - Optional[ListNode]

        @Example:
        >>> l1 = [2, 4, 3]
        >>> l2 = [5, 6, 4]
        >>> add_two_numbers(l1, l2)
        [7, 0, 8]
        """
        def validate_list_node(node):
            current = node
            while current:
                if not isinstance(current.val, int):
                    raise ValueError("Input must be a list of integers")
                current = current.next

        validate_list_node(l1)
        validate_list_node(l2)
            
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = carry + x + y
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy_head.next

def main():
    l1 = [2, 4, 3]
    l1 = ListNode().list_to_nodes(l1)
    l2 = [5, 6, 4]
    l2 = ListNode().list_to_nodes(l2)
    result = Solution().add_two_numbers(l1, l2)
    print(ListNode().nodes_to_list(result))

if __name__ == "__main__":
    main()
