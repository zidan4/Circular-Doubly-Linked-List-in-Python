if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    # Append nodes
    cdll.append(10)
    cdll.append(20)
    cdll.append(30)
    cdll.append(40)

    print("Forward Traversal:")
    cdll.display()  # Output: 10 <-> 20 <-> 30 <-> 40 <-> (back to head)

    print("\nReverse Traversal:")
    cdll.display_reverse()  # Output: 40 <-> 30 <-> 20 <-> 10 <-> (back to tail)

    # Delete a node
    cdll.delete(20)
    cdll.display()  # Output: 10 <-> 30 <-> 40 <-> (back to head)

    # Cycle detection (always true for circular lists)
    print("\nCycle detected:", cdll.detect_cycle())  # Output: True

