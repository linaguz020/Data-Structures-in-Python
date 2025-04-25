import HashTable

hash_table = HashTable.HashTable(4)
bridesmaids = [[1234, "Angelina"], [3456, "Lilliana"], [2717, "Gia"], [9012, "Ariana"], [8432, "Cleo"]]
for bridesmaid in bridesmaids:
    hash_table.insert(bridesmaid[0], bridesmaid[1])
print(hash_table.search(8432))