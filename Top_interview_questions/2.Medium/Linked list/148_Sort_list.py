class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end = " -> ")
        current = current.next

def merge(l, r):
    dummy = current = ListNode(0)
    while l and r:
        if l.val < r.val:
            current.next = l
            l = l.next
        else:
            current.next = r
            r = r.next
        current = current.next
    if not l:
        current.next = r
    if not r:
        current.next = l
    return dummy.next

def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    start = slow.next
    slow.next = None
    l, r = sort_list(head), sort_list(start)
    return merge(l, r)

if __name__ == "__main__":
    ll = ListNode(4)
    ll.next = ListNode(2)
    ll.next.next = ListNode(1)
    ll.next.next.next = ListNode(3)

    ans = sort_list(ll)
    print_linked_list(ans)
