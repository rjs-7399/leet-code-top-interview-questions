'''This is my logc
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def create_linked_list(arr,skip_index):
    if not arr:
        return None
    head = ListNode(arr[skip_index])
    current = head
    for i in range(skip_index+1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def inter_section_of_two_linked_list(current1,current2):
    while current1 and current2:
        print("Current1 node : {}".format(current1.value))
        print("Current2 node : {}".format(current2.value))
        print(current1.value == current2.value)
        if current1 == current2:
            return current1
        current1 = current1.next
        current2 = current2.next
    return None


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

array1 = [4, 1, 8, 4, 5]
array2 = [5, 6, 1, 8, 5]

linked_list_1_head = create_linked_list(array1,2)
linked_list_2_head = create_linked_list(array2,3)

print("Linked list 1:")
print_linked_list(linked_list_1_head)

print("Linked list 2:")
print_linked_list(linked_list_2_head)

intersected_node = inter_section_of_two_linked_list(linked_list_1_head,linked_list_2_head)

'''