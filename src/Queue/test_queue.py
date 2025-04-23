import unittest
import Queue

class TestQueue(unittest.TestCase):
    def create_sample_queue(self):
        vals = [3, -1, 4, 9, 10]
        queue = Queue.Queue()

        for val in vals:
            queue.enqueue(val)

        return queue
    
    def test_eneque(self):
        queue = self.create_sample_queue()
        self.assertEqual(queue.printQueue(), [3,-1,4,9,10])
        queue = Queue.Queue()
        self.assertEqual(queue.printQueue(), [])

    def test_dequeue(self):
        queue = self.create_sample_queue()
        queue.dequeue()
        self.assertEqual(queue.printQueue(), [-1,4,9,10])
        queue = Queue.Queue()
        queue.dequeue()
        self.assertEqual(queue.printQueue(), [])
    
    def test_front(self):
        queue = self.create_sample_queue()
        self.assertEqual(queue.front(), 3)
        queue = Queue.Queue()
        self.assertEqual(queue.front(), None)

    def test_back(self):
        queue = self.create_sample_queue()
        self.assertEqual(queue.back(), 10)
        queue = Queue.Queue()
        self.assertEqual(queue.back(), None)

if __name__ == '__main__':
    unittest.main()