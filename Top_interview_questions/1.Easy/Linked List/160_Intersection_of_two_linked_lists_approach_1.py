class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next


def get_intersection_of_two_linked_list(headA, headB):
    def find_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    length1 = find_length(headA)
    length2 = find_length(headB)

    if length1 > length2:
        for _ in range(length1 - length2):
            headA = headA.next
    else:
        for _ in range(length2 - length1):
            headB = headB.next

    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

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

    ans = get_intersection_of_two_linked_list(ll1, ll2)
    print(ans.val)