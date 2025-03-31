"""First task"""
def stringify(node):
    """
    a function stringify which accepts 
    an argument list / $list and returns a 
    string representation of the list.
    """
    current = node
    if current is None:
        return "None"
    result = str(current.data)
    while True:
        result += " -> " 
        current = current.next
        result += str(current.data) if current is not None else "None"
        if current is None:
            break
    return result
