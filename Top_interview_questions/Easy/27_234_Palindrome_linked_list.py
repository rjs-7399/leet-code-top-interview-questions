class ListNode:
    def __init__(self,key):
        self.next = None
        self.val = key

def add_to_stack(head,stack):
    current = head
    while current:
        stack.append(current.val)
        current = current.next

def check_palindrome(head,stack):
    current = head
    while current:
        element = stack.pop()
        if element != current.val:
            return False
        current = current.next
    return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)

    input_stack = []
    add_to_stack(head, input_stack)
    print(input_stack)
    ans = check_palindrome(head, input_stack)
    print(ans)