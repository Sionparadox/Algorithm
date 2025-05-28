import sys
input = sys.stdin.readline

letters = list(input().strip())
query = input().strip()

words = set()

for c in letters:
    for i in range(len(query)):
        words.add(query[:i]+c+query[i+1:])
        words.add(query[:i]+c+query[i:])
        words.add(query[:i]+query[i+1:])
    words.add(query+c)
words.remove(query)
print('\n'.join(sorted(list(words))))