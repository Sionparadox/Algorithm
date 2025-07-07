import bisect
def solution(words, queries):
    answer = []
    words_dict = {}
    reversed_words_dict = {}
    
    for word in words:
        L = len(word)
        words_dict.setdefault(L, []).append(word)
        reversed_words_dict.setdefault(L, []).append(word[::-1])
    
    for l in words_dict:
        words_dict[l].sort()
        reversed_words_dict[l].sort()
    
    for query in queries:
        L = len(query)
        if L not in words_dict:
            answer.append(0)
            continue
        
        if query[0] != '?':
            left = query.replace('?', 'a')
            right = query.replace('?', 'z')
            arr = words_dict[L]
        else:
            left = query[::-1].replace('?', 'a')
            right = query[::-1].replace('?', 'z')
            arr = reversed_words_dict[L]
        
        res = bisect.bisect_right(arr, right) - bisect.bisect_left(arr, left)
        answer.append(res)

    return answer