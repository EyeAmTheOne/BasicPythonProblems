#Check if the given word is a palindrome

input_word = input("Enter a word to see if it is a palindrome: ")
print(input_word[::-1].strip())

def isPalindrome(word: str):
    if word[::-1].strip() == word.strip():
        return True
    else:
        return False
    
print(isPalindrome(input_word))