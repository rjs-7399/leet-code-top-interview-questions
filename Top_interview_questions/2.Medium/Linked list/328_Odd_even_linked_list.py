class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def merge_two_linked_list(head1, head2):
    temp = head1
    current1, current2 = head1, head2
    while current1.next:
        current1 = current1.next
    current1.next = current2
    return temp


def separate_odd_even_index(head):
    current = head
    odd_head = ListNode(0)
    even_head = ListNode(0)
    odd_list, even_list = odd_head, even_head
    index = 1
    while current:
        if index%2 == 0:
            even_list.next = current
            even_list = even_list.next
        else:
            odd_list.next = current
            odd_list = odd_list.next
        current = current.next
        index += 1
    odd_list.next = None
    even_list.next = None
    return merge_two_linked_list(odd_head.next, even_head.next)

if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)
    print_linked_list(separate_odd_even_index(ll))