'''
You are given a singly linked list and an integer k.

Return the linked list, removing the k-th last element from the list.

Try to do it in a single pass and using constant space.
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_from_linked_list(head, k):
    curr = head
    k_away = head
    for i in range(k):
        k_away = k_away.next

    while (k_away.next != None):
        curr = curr.next
        k_away = k_away.next

    curr.next = curr.next.next
    return head

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]
