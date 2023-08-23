class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next

def add_two_numbers(l1, l2):
    v1 = v2 = carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

if __name__ == "__main__":
    ll1 = ListNode(9)
    ll1.next = ListNode(9)
    ll1.next.next = ListNode(9)
    ll1.next.next.next = ListNode(9)
    ll1.next.next.next.next = ListNode(9)
    ll1.next.next.next.next.next = ListNode(9)
    ll1.next.next.next.next.next.next = ListNode(9)

    ll2 = ListNode(9)
    ll2.next = ListNode(9)
    ll2.next.next = ListNode(9)
    ll2.next.next.next = ListNode(9)

    ans = add_two_numbers(ll1, ll2)
    print_linked_list(ans)
