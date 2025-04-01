"""Module for push and build_one_two_three functions."""
class Node:
    """Node class for linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    """Function push which accepts a head and data"""
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    """Function build_one_two_three which returns a linked list"""
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
