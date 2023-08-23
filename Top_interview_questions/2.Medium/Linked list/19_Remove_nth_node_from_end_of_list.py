class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print(" None ")

def get_length(head):
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    return length

def remove_nth_node_from_end(head, index):
    if head:
        current = head
        if index == 0:
            current = current.next
            return current
        else:
            temp = ListNode(0)
            temp.next = current = head
            length = 0
            while current:
                length += 1
                if index == length:
                    current.next = current.next.next
                current = current.next
            return temp.next
    else:
        return None


if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)
    input_index = 1
    delete_index = get_length(ll) - input_index
    result_list = remove_nth_node_from_end(ll, delete_index)
    print_linked_list(result_list)