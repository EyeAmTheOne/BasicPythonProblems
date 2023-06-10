import testing

#Print the overlapping elements of two given lists

list1, list2 = testing.generate_test_pairs()
print(list1, list2)

def overlap(a: list, b: list):
    return list(set([x for x in a if x in b]))

print(overlap(list1, list2))