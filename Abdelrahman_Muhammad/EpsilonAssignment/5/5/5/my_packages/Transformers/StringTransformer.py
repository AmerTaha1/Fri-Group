def reverse(word):
    s = word[::-1]
    return s
    pass

def capital(word):
    s = []
    for i in word:
        s.append(i.capitalize())
    print(''.join(s))
    pass