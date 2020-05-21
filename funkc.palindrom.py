def palindrom(b):
    print('введите палиндром')
    b = str(input())
    a = b.replace(' ', '')
    c = 'палиндром'
    l = 'не палиндром'
    if a[0:] == a[::-1]:
        return c
    else:
        return l
        
print(palindrom(''))