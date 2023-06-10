import random

def generate_test_pairs(length=10, overlap=5):
    list1 = random.sample(range(1, length * 2), length)
    common_values = random.sample(list1, overlap)
    list2 = random.sample(common_values + list(set(range(1, length * 2)) - set(list1)), length)
    return list1, list2