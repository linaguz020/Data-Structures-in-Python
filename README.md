# Data Structures in Python

This project is designed to practice and showcase my understanding of data structures in Python. It includes implementations of various data structures along with unit tests to ensure the correctness of the code.

## Current Progress

### LinkedList
I have implemented a `LinkedList` class with the following functionalities:
- **add(item)**: Adds element to end of the list.
- **insert(item, index)**: Add a new element to the list. If the index is not valid, it will add the element to the beginning or end depending on the index.
- **delete()**: Remove an element from the list.
- **search(item)**: Returns true if an element is in the list.
- **size()**: Get the number of elements in the list.
- **printList()**: Prints the elements in the Linked List as a list.
- **combine(linked_list)**: Join two linked lists into one.

### Stack
The `Stack` class implements a basic stack data structure using the Last-In-First-Out (LIFO) principle. It provides the following methods:
- **push(item)**: Adds an element to the top of the stack
- **pop**: Removes element at the top of the stack and returns top element
- **top**: Returns the element at the top of the stack
- **empty**: Returns true if the element is empty
- **size**: Returns the number of elements currently in the stack.
- **printStack**: Prints the elements in the stack as a list.

### Queue

The `Queue` class implements a basic queue data structure using the First-In-First-Out (FIFO) principle. It provides the following methods:

- **enqueue(item)**: Adds an item to the back of the queue.
- **dequeue()**: Removes and returns the item at the front of the queue. If the queue is empty, it returns `None` or raises an appropriate exception.
- **front()**: Returns the item at the front of the queue without removing it. If the queue is empty, it returns `None`.
- **back()**: Returns the item at the back of the queue without removing it. If the queue is empty, it returns `None`.
- **size()**: Returns the number of items currently in the queue.
- **printQueue()**: Prints all the elements in the queue in order from front to back.

## Testing
All functionalities are thoroughly tested using Python's `unittest` framework to ensure reliability and correctness.

## Future Plans
I plan to implement additional data structures such as:
- Trees
- Graphs
- Hash Tables

Stay tuned for updates as I continue to expand this project!

## How to Run
1. Clone this repository.
2. Navigate to the project directory.
3. Run the tests using:
    ```bash
    python3 -m unittest discover
    ```
---
Feel free to explore the code and provide feedback!