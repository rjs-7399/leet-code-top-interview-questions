class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next

if __name__ == "__main__":
    l = [1,2,3,4]
    ll = temp = ListNode(0)
    for element in l:
        ll.next = ListNode(element)
        ll = ll.next
    print_linked_list(temp.next)