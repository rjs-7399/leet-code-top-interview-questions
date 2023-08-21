class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        if self.is_empty() or self.head.next is None:
            return
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def display(self):
        if self.is_empty():
            print("LinkedList is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


my_list = [1, 2, 3, 4, 5]
linked_list = LinkedList()

for item in my_list:
    linked_list.append(item)

print("Original Linked List:")
linked_list.display()

linked_list.reverse()

print("Reversed Linked List:")
linked_list.display()