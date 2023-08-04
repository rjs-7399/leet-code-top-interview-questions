class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def delete_node_linked_list(head,del_node):
    if head.val == del_node:
        current = head.next
        head.next = None
        head = current
        print(head.val)
    else:
        current = head
        while current.next:
            if current.next.val == del_node:
                current.next = current.next.next
            else:
                current = current.next
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    delete_node_linked_list(head,1)
    print_linked_list(head)