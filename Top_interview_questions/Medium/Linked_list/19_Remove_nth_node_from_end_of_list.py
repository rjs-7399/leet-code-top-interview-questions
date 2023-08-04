class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_length(head):
    l = 0
    current = head
    while current:
        l += 1
        current = current.next
    return l


def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def delete_nth_node(head,n):
    current = head
    if n == 0:
        return current.next
    else:
        x = 0
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while x < n:
            prev = prev.next
            current = current.next
            x += 1
        prev.next = prev.next.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    delete_node_from_end = 5

    print("Print linked list :")
    print_linked_list(head)
    print("Get length of linked list :")
    length_ll = get_length(head)
    print(length_ll)

    delete_index = length_ll-delete_node_from_end
    print("Print linked list after deletion :")
    ans = delete_nth_node(head,delete_index)
    print_linked_list(ans)