class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    if head == None:
        return
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end= " -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    print_linked_list(ll)
    reversed_ll = reverse_linked_list(ll)
    print_linked_list(reversed_ll)
