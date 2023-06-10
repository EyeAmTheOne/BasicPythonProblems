#Prints out all the elements of a given list that are less than a given number.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 9, 12, 4, 6, 2]

limit = int(input("Enter a limit: "))

def lessThanFive(list, num=5):
    return [x for x in list if x < num]

print(lessThanFive(a, limit))