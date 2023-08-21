class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_two_sorted_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2
    return dummy.next
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print("Null")

if __name__ == "__main__":
    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(4)
    ll1.next.next.next = ListNode(5)
    ll1.next.next.next.next = ListNode(6)
    ll2 = ListNode(1)
    ll2.next = ListNode(3)
    ll2.next.next = ListNode(4)

    print("Printing First list : ")
    print_linked_list(ll1)

    print("Printing Second list : ")
    print_linked_list(ll2)

    result_list = merge_two_sorted_lists(ll1, ll2)
    print_linked_list(result_list)