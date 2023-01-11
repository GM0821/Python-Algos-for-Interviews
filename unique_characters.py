def unique(s):
    s = s.replace(' ','')
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True

print(unique('a b cdef'))

