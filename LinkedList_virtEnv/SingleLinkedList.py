class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string respresentation of the list.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with 'data' matching
        'key'. Return the element or 'None' if not found.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr                                         # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurence of 'key' in the list
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(lst)

    lst.prepend(23)
    lst.prepend('a')
    lst.prepend(42)
    lst.prepend('X')
    lst.append('the')
    lst.append('end')

    print(lst)

    print(lst.find('a'))
    print(lst.find('Z'))

    lst.reverse()
    print(lst)

    lst.remove('the')
    print(lst.remove(365))

    print(lst)