import numpy as np

G = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


B = np.array([[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],[1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],[0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],[1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],[1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],[1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],[0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],[0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],[0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],[1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],[0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])


H = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],[1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],[0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],[1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],[1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],[1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],[0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],[0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],[0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],[1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],[0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])


def encode_Golay(info):
    global G

    if type(info) == list:
        while len(info)<12:
            info=[0]+info
        return list(np.array(info).dot(G)% 2)
        

def find_weight(word):
    """
    input is bit vector
    output is Hamming weight
    """
    i = 0
    for letter in word:
        if letter != 0:
            i += 1
    return i


def decode_Golay(word):
    if type(word) == str:
        word = [int(i) for i in word]

    if find_weight(word) % 2 == 0:
        word += [1]
    else:
        word += [0]

    c = decode_extended_Golay(word)
    return c

def decode_extended_Golay(word):
    if type(word) == str:
        word = [int(i) for i in word]

    global B
    global H

    s = list(word @ H % 2)
    if find_weight(s) <= 3:
        u = s + [0]*12
        # print(''.join(str(x) for x in u))
        sent_word = []
        for k in range(24):
            sent_word.append((word[k] + u[k]) % 2)
        return sent_word[:12]
    for i, row in enumerate(B):
        if find_weight([sum(z) % 2 for z in zip(s, list(row))]) <= 2:
            for j, value in enumerate(row):
                s[j] = (s[j] + value) % 2
            e_i = [0]*12
            e_i[i] = 1
            u = s + e_i
            # print(''.join(str(x) for x in u))
            sent_word = []
            for k in range(24):
                sent_word.append((word[k] + u[k]) % 2)
            return sent_word[:12]
    s = list(s @ B % 2)
    if find_weight(s) <= 3:
        u = [0]*12 + s
        # print(''.join(str(x) for x in u))
        sent_word = []
        for k in range(24):
            sent_word.append((word[k] + u[k]) % 2)
        return sent_word[:12]
    for i, row in enumerate(B):
        if find_weight([sum(z) % 2 for z in zip(s, list(row))]) <= 2:
            for j, value in enumerate(row):
                s[j] = (s[j] + value) % 2
            e_i = [0]*12
            e_i[i] = 1
            u = e_i + s
            # print(''.join(str(x) for x in u))
            sent_word = []
            for k in range(24):
                sent_word.append((word[k] + u[k]) % 2)
            return sent_word[:12]
    return 'request retransmission'
