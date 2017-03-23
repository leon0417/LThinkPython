
def inverse_letters(str):
    for n in range(len(str)):
        print(str[-(n + 1)])

def duck_name():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if 'O' == letter or 'Q' == letter:
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)

def slice_str(str):
    print(str[:])

def find(word, letter, index):
    for n in range(index, len(word)):
        if word[n] == letter:
            return n
    return -1

def count_letter(word, ch):
    cnt = 0
    for letter in word:
        if letter == ch:
            cnt = cnt + 1
    return cnt

def recount_letter(word, letter):
    cnt = 0
    index = 0
    while True:
        n = find(word, letter, index)
        if -1 != n:
            cnt = cnt + 1
            index = n + 1
        else:
            return cnt

def is_palindrome(str):
    return str[::1] == str[::-1]

def rotate_word(str, n):
    newWord = ''
    letterList = "abcdefghijklmnopqrstuvwxyz"
    for ch in str:
        if ch.isupper():
            index = find(letterList, ch.lower(), 0)
            newWord += letterList[(index + n) % len(letterList)].upper()
        else:
            index = find(letterList, ch, 0)
            newWord += letterList[(index + n) % len(letterList)]
    return newWord

