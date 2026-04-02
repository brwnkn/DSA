def reverse(x):
    num = ''
    x = list(str(x))
    
    while x:
        num = num + str(x.pop())
    if int(num.strip('-')) < pow(-2, 31) or int(num.strip('-')) > pow(2, 31)-1:
        return 0
    else:
       try:
           return int(num)
       except ValueError:
           return -1 * int(num.strip('-'))
print(reverse( -123))

