def nth_to_last_element(n, head):
    """
    :param: n - nth to last element to find
    return the nth to last element in the linked list
    """
    if n == 0:
        return None
    if head is None:
        return None
    if head.next is None:
        return head
    current = head
    nth_to_last = head
    for i in range(n):
        if current.next is None:
            return None
        current = current.next
    while current.next is not None:
        current = current.next
        nth_to_last = nth_to_last.next
    return nth_to_last