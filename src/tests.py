import unittest
import LinkedList

# This class tests Linked List functions
class TestLinkedList(unittest.TestCase):
    def create_sample_list(self):
        new_list = LinkedList.LinkedList()
        for val in [12, 14, 13, 20]:
            new_list.add(val)
        return new_list

    def test_empty_list_returns_empty_array(self):
        empty_list = LinkedList.LinkedList()
        self.assertEqual(empty_list.printList(), [])

    def test_filled_list_returns_correct_values(self):
        new_list = self.create_sample_list()
        self.assertEqual(new_list.printList(), [12, 14, 13, 20])

    def test_add_to_empty_list(self):
        new_list = LinkedList.LinkedList()
        new_list.add(12)
        self.assertEqual(new_list.printList(), [12])

    def test_add_to_filled_list(self):
        new_list = self.create_sample_list()
        self.assertEqual(new_list.printList(), [12, 14, 13, 20])

    def test_empty_list_size(self):
        new_list = LinkedList.LinkedList()
        self.assertEqual(new_list.size(), 0)

    def test_filled_list_size(self):
        new_list = self.create_sample_list()
        self.assertEqual(new_list.size(), 4)

    def test_search_empty_list(self):
        empty_list = LinkedList.LinkedList()
        self.assertEqual(empty_list.search(12), False)

    def test_search_known_val_filled_list(self):
        new_list = self.create_sample_list()
        self.assertEqual(new_list.search(12), True)
    
    def test_search_missing_val_filled_list(self):
        new_list = self.create_sample_list()
        self.assertEqual(new_list.search(-1), False)


if __name__ == '__main__':
    unittest.main()
