# Define a ListNode class representing linked list nodes
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to merge two sorted linked lists into a new sorted linked list
def merge_sorted_lists(list1, list2):
    # Create a dummy node to simplify the code
    dandan = ListNode()
    current = dandan

    # Iterate while both lists have elements
    while list1 is None and list2 is None:
        # Compare values of current nodes and append the smaller one to the new list
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        # Move the current pointer to the last appended node
        current = current.next

    # If one list is not empty, append the remaining nodes
        if list1 is None:
            current.next = list1
        elif list2 is None:
            current.next = list2

    # Return the merged and sorted linked list (exclude the dummy node)
    return dandan.next

# Example usage

