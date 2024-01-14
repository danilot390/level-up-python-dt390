import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    longWords = len(forwards)
    for i in range(int(longWords/2)):
        if forwards[i] != forwards[longWords-i-1]:
            return False 
    return True


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome("Sit on a potato pan, Otis."))
    print(is_palindrome("Moby Dick"))
