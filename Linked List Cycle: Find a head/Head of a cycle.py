# Node class
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# First we find out if there is a cycle. If there is - we can count its length
def find_length_cycle(head):
    slow = fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_cycle_length(slow)
    return None

# Function for counting the length of the cycle
def calculate_cycle_length(head):
    pointer = head
    cycle_length = 0
    while True:
        pointer = pointer.next
        cycle_length += 1
        if pointer == head:
            break
    return cycle_length


def find_cycle_start(head):
    if find_length_cycle(head) is None:
        return None
    cycle_length = find_length_cycle(head)
    slow = fast = head
    # We iterate through the list: if we go from current Node n steps ahead (where n == cycle length),
    # we'll encounter the same node again
    while True:
        count = 1
        while count < cycle_length + 1:
            fast = fast.next
            count += 1
        if fast == slow:
            return slow
        slow = slow.next
        fast = slow
    return head
