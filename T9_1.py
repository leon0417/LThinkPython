from T8_1 import *

def len_larger_than_N(path, N):
    fin = open(path)
    for line in fin:
        if N < len(line.strip()):
            print(line.strip())

def words_no_e(path):
    fin = open(path)
    cnt = 0
    sum = 0
    for line in fin:
        sum += 1
        if -1 == find(line.strip(), 'e', 0):
            print(line.strip())
            cnt += 1
    per = int(float(cnt) / float(sum) * 100)
    print("%d%%" %per)

def avoids(avoid, str):
    for letter in avoid:
        if -1 != find(str, letter, 0):
            return False
        if -1 != find(str, letter.upper(), 0):
            return False
    return True

def input_avoids(path):
    avoidsStr = input("Please input a string for avoids\n")
    fin = open(path)
    for line in fin:
        if avoids(avoidsStr, line.strip()):
            print(line.strip())

def uses_only(str, word):
    if avoids(word, str):
        return False
    else:
        return True

def check_sentence(str, sentence):
    for letter in sentence:
        if letter.isalpha() and letter.islower():
            if -1 == find(str, letter, 0) and -1 == find(str, letter.upper(), 0):
                return False
        elif letter.isalpha() and letter.isupper():
            if -1 == find(str, letter, 0) and -1 == find(str, letter.lower(), 0):
                return False
    return True

def uses_all(str, word):
    for letter in str:
        if -1 == find(word, letter, 0):
            return False
    return True

def check_words(path, str):
    fin = open(path)
    cnt = 0
    for line in fin:
        if uses_all(str, line.strip()):
            cnt += 1
            print(line.strip())
    print("the number of containing all letters is %d" % cnt)

def is_abecedarian(word):
    for i in range(len(word) - 1):
        if 0 > ord(word[i + 1]) - ord(word[i]):
            return False
    return True

def check_abecedarian(path):
    fin = open(path)
    cnt = 0
    for line in fin:
        if is_abecedarian(line.strip()):
            cnt += 1
            print(line.strip())
    print("The number of abecedarian is %d" % cnt)

def is_triple_double(word):
    i = 0
    cnt = 0
    if 6 > len(word):
        return False
    else:
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                cnt += 1
                i += 2
            else:
                cnt = 0
                i += 1
            if cnt == 3:
                return True
    return False

def car_talk_one(path):
    fin = open('words.txt')
    for line in fin:
        if is_triple_double(line.strip()):
            print(line.strip())

def is_reverse(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

def is_triple_reverse(num):
    if 100000 > num or 999996 < num:
        print("wrong number!")
        return False
    newStr = str(num)
    i = 2
    if is_reverse(newStr[2:]):
        newStr = str(num + 1)
    else:
        return False

    if is_reverse(newStr[1:]):
        newStr = str(num + 2)
    else:
        return False

    if is_reverse(newStr[1:5]):
        newStr = str(num + 3)
    else:
        return False

    if is_reverse(newStr[:]):
        newStr = str(num + 4)
    else:
        return False
    return True


def car_talk_two():
    for i in range(100000, 999996):
        if is_triple_reverse(i):
            print(i)


