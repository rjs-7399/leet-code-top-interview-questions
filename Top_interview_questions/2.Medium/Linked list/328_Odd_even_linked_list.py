class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_two_list(l1, l2):
    current = l1
    while current.next:
        current = current.next
    current.next = l2
    return l1

def get_odd_even(head):
    current = head
    odd_head = ListNode(0)
    even_head = ListNode(0)
    odd = odd_head
    even = even_head
    index = 0
    while current:

        if index%2 == 0:
            odd.next = current
            odd = odd.next
            print("odd Index : {}, Val : {}".format(index, odd.val))
        if index%2 != 0:
            even.next = current
            even = even.next
            print("even Index : {}, Val : {}".format(index, even.val))
        current = current.next
        index += 1
    odd.next = None
    even.next = None
    return odd_head.next,even_head.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next


if __name__ == "__main__":
    head1 = ListNode(2)
    head1.next = ListNode(1)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(5)
    head1.next.next.next.next = ListNode(6)
    head1.next.next.next.next.next = ListNode(4)
    head1.next.next.next.next.next.next = ListNode(7)
    odds,evens = get_odd_even(head1)

    print("Printing elements at odd indices :")
    print_linked_list(odds)
    print()
    print("Printing elements at even indices :")
    print_linked_list(evens)
    ans = merge_two_list(odds, evens)
    print("Printing Merge linked list :")
    print_linked_list(ans)