
import time
import random


# Array and Dynamic Array

def array_comparison():
    print("\n--- ARRAY AND DYNAMIC ARRAY ---")

    sizes = [1000, 5000, 10000]

    for size in sizes:
        data = list(range(size))

        # Search
        start = time.perf_counter()
        data.index(size - 1)
        array_search = time.perf_counter() - start

        # Insertion
        start = time.perf_counter()
        data.insert(0, -1)
        array_insert = time.perf_counter() - start

        # Deletion
        start = time.perf_counter()
        data.pop(0)
        array_delete = time.perf_counter() - start

        print(f"\nData size: {size}")
        print(f"Search time: {array_search:.8f} seconds")
        print(f"Insertion time: {array_insert:.8f} seconds")
        print(f"Deletion time: {array_delete:.8f} seconds")


# Singly and Doubly Linked Lists

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = SinglyNode(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, value):
        current = self.head
        previous = None

        while current:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete(self, value):
        current = self.head

        while current:
            if current.data == value:

                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True

            current = current.next

        return False

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


def linked_list_comparison():
    print("\n--- LINKED LISTS ---")

    singly = SinglyLinkedList()
    doubly = DoublyLinkedList()

    for i in range(1, 6):
        singly.insert(i)
        doubly.insert(i)

    print("\nSingly Linked List:")
    singly.display()

    print("\nDoubly Linked List:")
    doubly.display()

    print("\nSearch for 3:")
    print("Singly:", singly.search(3))
    print("Doubly:", doubly.search(3))

    print("\nDelete 3:")
    singly.delete(3)
    doubly.delete(3)

    print("Singly after deletion:")
    singly.display()

    print("Doubly after deletion:")
    doubly.display()


# Stack, Queue and Deque

from collections import deque


def stack_example():
    print("\n--- STACK ---")

    stack = []

    # Add elements
    stack.append("Page 1")
    stack.append("Page 2")
    stack.append("Page 3")

    print("Stack:", stack)

    # Last In, First Out (LIFO)
    print("Back button:", stack.pop())
    print("Current stack:", stack)


def queue_example():
    print("\n--- QUEUE ---")

    queue = deque()

    # Add customers
    queue.append("Customer 1")
    queue.append("Customer 2")
    queue.append("Customer 3")

    print("Queue:", list(queue))

    # First In, First Out (FIFO)
    print("Serving:", queue.popleft())
    print("Remaining queue:", list(queue))


def deque_example():
    print("\n--- DEQUE ---")

    items = deque()

    # Add from both sides
    items.append("Task 1")
    items.append("Task 2")
    items.appendleft("Urgent Task")

    print("Deque:", list(items))

    # Remove from both sides
    print("Remove from front:", items.popleft())
    print("Remove from back:", items.pop())

    print("Remaining deque:", list(items))


def stack_queue_deque():
    stack_example()
    queue_example()
    deque_example()


# MAIN MENU

def main():

    while True:

        print("\n================================")
        print("       DATA STRUCTURES PROJECT")
        print("================================")

        print("1. Array and Dynamic Array")
        print("2. Singly and Doubly Linked Lists")
        print("3. Stack, Queue and Deque")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            array_comparison()

        elif choice == "2":
            linked_list_comparison()

        elif choice == "3":
            stack_queue_deque()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
