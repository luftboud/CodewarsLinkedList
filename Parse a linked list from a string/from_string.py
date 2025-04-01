"""module from_string.py which contains a function
linked_list_from_string that accepts a string argument
$s and returns a linked list representation of the string.
"""
class Node:
    """Node class for linked list"""
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """function linked_list_from_string which accepts
    a string argument $s and returns a linked list
    representation of the string.
    """
    nodes = s.split("->")[::-1][1:]
    head = None
    for n in nodes:
        head = Node(int(n),head)

    return head
