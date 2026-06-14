def isPalindrome(s):
    if len(s) == 1 or s == '':
        return True
    return s[0] == s[-1] and isPalindrome(s[1:-1])