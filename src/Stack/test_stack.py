import unittest
import Stack

class TestStack(unittest.TestCase):
    def create_sample_stack(self):
        stack1 = Stack.Stack()
        vals = [12, 14, 16, 18, 20]
        for val in vals:
            stack1.push(val)
        return stack1
    
    def test_push_vals(self):
        stack = self.create_sample_stack()
        self.assertEqual(stack.printStack(), [12, 14, 16, 18, 20])

    def test_empty(self):
        stack = self.create_sample_stack()
        self.assertEqual(stack.empty(), False)
        stack = Stack.Stack()
        self.assertEqual(stack.empty(), True)

    def test_print_empty_stack(self):
        stack = Stack.Stack()
        self.assertEqual(stack.printStack(), [])

    def test_size(self):
        stack = self.create_sample_stack()
        self.assertEqual(stack.size(), 5)
        stack = Stack.Stack()
        self.assertEqual(stack.size(), 0)

    def test_pop(self):
        stack = self.create_sample_stack()
        self.assertEqual(stack.pop(), 20, "does not correctly pop last element")
        stack = Stack.Stack()
        self.assertEqual(stack.pop(), None, "does not correctly handle popping on empty list")

    def test_top(self):
        stack = self.create_sample_stack()
        self.assertEqual(stack.top(), 20)
        stack = Stack.Stack()
        self.assertEqual(stack.top(), None)


if __name__ == '__main__':
    unittest.main()