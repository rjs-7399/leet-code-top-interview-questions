class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_intersection_of_two_linked_lists(head1, head2):
    pA = head1
    pB = head2

    while pA is not pB:
        if pA.next == None:
            pA = head2
        else:
            pA = pA.next
        if pB.next == None:
            pB = head1
        else:
            pB = pB.next
    return pA

if __name__ == "__main__":
    ll1 = ListNode(4)
    ll1.next = ListNode(1)
    ll1.next.next = ListNode(8)
    ll1.next.next.next = ListNode(4)
    ll1.next.next.next.next = ListNode(5)

    ll2 = ListNode(5)
    ll2.next = ListNode(6)
    ll2.next.next = ListNode(1)
    ll2.next.next.next = ll1.next.next

    intersected_value = get_intersection_of_two_linked_lists(ll1, ll2)
    print(intersected_value.val)