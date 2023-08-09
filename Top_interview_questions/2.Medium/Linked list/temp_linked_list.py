class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def merge(l, r):
    dummy = tail = ListNode(0)
    while l and r:
        if l.val <= r.val:
            tail.next = l
            l = l.next
        else:
            tail.next = r
            r = r.next
        tail = tail.next
    tail.next = l or r
    return dummy.next

def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    l, r = mergeKLists(lists[:mid]), mergeKLists(lists[mid:])
    return merge(l, r)



if __name__ == "__main__":
    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(7)

    ll2 = ListNode(4)
    ll2.next = ListNode(5)
    ll2.next.next = ListNode(9)

    ll3 = ListNode(3)
    ll3.next = ListNode(6)
    ll3.next.next = ListNode(8)

    lists = []
    lists.append(ll1)
    lists.append(ll2)
    lists.append(ll3)

    sorted_list = mergeKLists(lists)
    print_linked_list(sorted_list)
