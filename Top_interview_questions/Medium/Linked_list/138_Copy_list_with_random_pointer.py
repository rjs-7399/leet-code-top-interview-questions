class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def deep_copy_linked_list(head):
    if not head:
        return None

    old_to_new = {}
    current = head
    while current:
        new_node = ListNode(current.val)
        old_to_new[current] = new_node
        current = current.next

    current = head
    while current:
        new_node = old_to_new[current]
        new_node.next = old_to_new.get(current.next)
        current = current.next

    current = head
    while current:
        new_node = old_to_new[current]
        new_node.random = old_to_new.get(current.random)
        current = current.next

    return old_to_new[head]

if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    node1.random = node3
    node2.random = node1
    node3.random = node2

    # Performing deep copy
    new_head = deep_copy_linked_list(node1)

    # Testing the deep copy result
    print("Original list:")
    current = node1
    while current:
        print(f"Node {current.val}, Random -> {current.random.val if current.random else 'None'}")
        current = current.next

    print("Deep copied list:")
    current = new_head
    while current:
        print(f"Node {current.val}, Random -> {current.random.val if current.random else 'None'}")
        current = current.next
