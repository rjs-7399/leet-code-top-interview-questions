class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def array_to_list(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
    return head


def list_to_array(head):
    l = []
    current = head
    while current:
        l.append(current.data)
        current = current.next
    return l

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def create_linked_list_from_array(arr):
    head = None
    for element in arr:
        head = array_to_list(head, element)
    return head


# Example usage:
if __name__ == "__main__":
    array1 = [2, 4, 9]
    array2 = [5, 6, 4, 9]
    ll1 = create_linked_list_from_array(array1)
    ll2 = create_linked_list_from_array(array2)
    display(ll1)
    display(ll2)
    l1 = list_to_array(ll1)
    l2 = list_to_array(ll2)
    str1 = "".join(str(element) for element in l1)
    str2 = "".join(str(element) for element in l2)
    str1 = str1[::-1]
    str2 = str2[::-1]
    ans = str(int(str1) + int(str2))
    ans = ans[::-1]
    print(ans)

    head = None
    for i in range(len(ans)):
        head = array_to_list(head, ans[i])
    final_ll = head
    print(final_ll.data)