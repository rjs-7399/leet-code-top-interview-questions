class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def cycle_detection(head):
    slow = fast = head
    while slow != None and fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(5)
    list1.next.next.next.next.next = list1.next.next
    print(cycle_detection(list1))