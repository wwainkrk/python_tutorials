class ListNode:
    """
    A node in a doubly-linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        """
        Create a new doubly linked list.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Add a new element at the beginning of the list.
        """
        new_head = ListNode(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def append(self, data):
        """
        Add a new element at the end of the list.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data, prev=curr)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        The same method as in single-linked list.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr                                         # Will be None if not found

    def remove_elem(self, node):
        """
        Unlink an element from the list.
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        """
        elem = self.find(key)
        if not elem:
            return
        self.remove_elem(elem)

    def reverse(self):
        """
        Reverse the list in-place. Using temporary variable.
        """
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        self.head = prev_node.prev


if __name__ == "__main__":
    lst = DoublyLinkedList()
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

    elem1 = lst.find('the')
    print(elem1)
    lst.remove_elem(elem1)

    print(lst)

    elem2 = lst.find(365)
    print(elem2)
    lst.remove(elem2)

    print(lst)
