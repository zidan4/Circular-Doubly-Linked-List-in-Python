class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        
        last_node = self.head.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        self.head.prev = new_node

    # Display forward
    def display(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    # Reverse traversal
    def display_reverse(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head.prev
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current == self.head.prev:
                break
        print("(back to tail)")

    # Delete a node
    def delete(self, key):
        if not self.head:
            return
        
        current = self.head
        while True:
            if current.data == key:
                if current == self.head and current.next == self.head:  # Only one node
                    self.head = None
                    break

                if current == self.head:  # Deleting head node
                    self.head = current.next

                current.prev.next = current.next
                current.next.prev = current.prev
                break
            
            current = current.next
            if current == self.head:
                break

    # Detect Cycle (always true for circular list)
    def detect_cycle(self):
        return True

