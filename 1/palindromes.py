#!python3

def is_palindrome(s: str):
    return s == s[::-1]

assert is_palindrome("")
assert is_palindrome("wow")
assert not is_palindrome("no")

