"""Module for get_nth function"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, n=None):
        self.data = data
        self.next = n

def get_nth(node, index):
    """
    Function get_nth which accepts a node and an index
    and returns the node at the index
    """
    if not isinstance(index, int) or index < 0 or node is None:
        raise Exception
    curr = node
    for _ in range(index):
        if curr.next is None:
            raise Exception
        curr = curr.next
    return curr
