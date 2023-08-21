class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def check_palindrom_list(head):
    current2 = head
    current1 = head
    stack = []
    while current1:
        stack.append(current1.val)
        current1 = current1.next
    while stack:
        if current2.val != stack.pop():
            return False
        current2 = current2.next
    return True

if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(2)
    ll.next.next.next.next = ListNode(1)

    ans = check_palindrom_list(ll)
    print(ans)