def pal(a):
    if a==a[::-1]:
        b='PALINDROME'
        return b
    else:
        c='NOT PALINDROME'
        return c
a=input('Give input: ')
print(pal(a))