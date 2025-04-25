import unittest
import HashTable

class TestHashTables(unittest.TestCase):
    def create_sample_hashtable(self):
        hash_table = HashTable.HashTable(4)
        names = [[1234, "Angelina"], [3456, "Lilliana"], [2717, "Gia"], [9012, "Ariana"], [8432, "Cleo"]]
        for name in names:
            hash_table.insert(name[0], name[1])
        return hash_table

    def test_search_hashtable(self):
        hash_table = self.create_sample_hashtable()
        empty = HashTable.HashTable(1)
        self.assertEqual(hash_table.search(3456), "Lilliana")
        self.assertEqual(empty.search(1234), None)

    def test_create_hash_table(self):
        hash_table = self.create_sample_hashtable()
        self.assertEqual(hash_table)


if __name__ == '__main__':
    unittest.main()