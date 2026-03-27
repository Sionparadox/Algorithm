import sys
input = sys.stdin.readline

mapper = {
    'a': 'aespa',
    'b': 'baekjoon',
    'c': 'cau',
    'd': 'debug',
    'e': 'edge',
    'f': 'firefox',
    'g': 'golang',
    'h': 'haegang',
    'i': 'iu',
    'j': 'java',
    'k': 'kotlin',
    'l': 'lol',
    'm': 'mips',
    'n': 'null',
    'o': 'os',
    'p': 'python',
    'q': 'query',
    'r': 'roka',
    's': 'solvedac',
    't': 'tod',
    'u': 'unix',
    'v': 'virus',
    'w': 'whale',
    'x': 'xcode',
    'y': 'yahoo',
    'z': 'zebra'
}

S = input().strip()
L = len(S)

word_list = []
idx = 0
while idx < L:
    c = S[idx]
    origin = mapper[c]
    if S.startswith(origin, idx):
        idx += len(origin)
        word_list.append(c) # 2. 리스트에 추가
    else:
        print("ERROR!")
        exit()

print("It's HG!")
print("".join(word_list))
