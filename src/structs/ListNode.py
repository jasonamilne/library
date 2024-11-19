class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
    def list_to_nodes(self, values):
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    def nodes_to_list(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values
