#Prints out all the divisors of a given number

number = int(input("Enter the number you want to find all the divisors of: "))

def divisor(num: int):
    return [x for x in range(1, num+1) if num % x == 0]

print(divisor(number))