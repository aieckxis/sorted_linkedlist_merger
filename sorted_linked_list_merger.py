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
    while list1 is not None and list2 is not None:
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
if __name__ == "__main__":
    # Create two sorted linked lists
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    # Merge the lists and get the result
    merged_list = merge_sorted_lists(list1, list2)

    # Print the merged list
    while merged_list is not None:
        print(merged_list.value, end=" -> ")
        merged_list = merged_list.next