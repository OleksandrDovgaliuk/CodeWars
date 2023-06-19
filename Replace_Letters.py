def replace_letters(word):
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

    vowels = ('a', 'e', 'i', 'o', 'u')

    for letter in word:
        index = alphabet.index(letter)
        if letter in vowels:
            arr = list(alphabet[:index]).reverse()
            for char in arr:
                if char in vowels:
                    word.replace(letter, char)
                else:
                    pass
        elif letter in consonants:
            arr = alphabet[index:]

    return word


print(replace_letters('cat'))
