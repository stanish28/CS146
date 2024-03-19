def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))
    
    s2 = "race a car"
    print(is_palindrome(s2))