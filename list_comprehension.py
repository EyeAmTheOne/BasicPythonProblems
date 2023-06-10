#Prints out the even numbers of a given list

inp_list = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,22]

def evenValues(list: list):
    return [x for x in list if x % 2 == 0]

print(evenValues(inp_list))