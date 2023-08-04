def deleteNode(self, node):
    node.val = node.next.val
    node = node.next