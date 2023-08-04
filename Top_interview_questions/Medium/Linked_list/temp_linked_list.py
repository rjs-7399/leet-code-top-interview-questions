from queue import PriorityQueue

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def mergeKLists(lists):
        i = 0
        dummy = ListNode(None)
        current = dummy
        q = PriorityQueue()
        for node in lists:
            i += 1
            if node:
                q.put((node.val,i,node))
        while q.qsize() > 0:
            i +=1
            current.next = q.get()[2]
            current = current.next
            if current.next:
                q.put((current.next.val, i, current.next))
        return dummy.next

if __name__ == "__main__":
    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)

    ll2 = ListNode(1)
    ll2.next = ListNode(3)
    ll2.next.next = ListNode(4)

    ll3 = ListNode(2)
    ll3.next = ListNode(4)
    ll3.next.next = ListNode(5)

    l = []
    l.append(ll1)
    l.append(ll2)
    l.append(ll3)

    temp_list = mergeKLists(l)
    print_linked_list(temp_list)