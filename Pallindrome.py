def isPalindrome(x):
    i = len(str(x)) -1
    reversed = str()
    while i >= 0:
        reversed += str(x)[i]
        i -=1
    if int(reversed) == x:
        return True
    else:
        return False
print(isPalindrome(121))
