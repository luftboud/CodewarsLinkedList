"""Module for move_node function"""
# from push_build:
def push(head, data):
    """Function push which accepts a head and data"""
    node = Node(data)
    node.next = head
    return node

class Node(object):
    """Node class for linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """Context class for linked list"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """Function move_node which accepts source and dest"""
    if source is None:
        raise Exception
    new_source = source.next
    node = push(dest, source.data)
    return Context(new_source, node)
