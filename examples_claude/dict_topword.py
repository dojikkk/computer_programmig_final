def topWord(words):
    words = sorted(words)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    mostword = None
    mostcount = 0
    for k, i in counts.items():
        if i > mostcount:
            mostword = k
            mostcount = i
    return mostword


def noneSortTopWord(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    best = None
    best_count = 0
    for word, count in counts.items():
        if count > best_count or (count == best_count and word < best): 

            # or 조건으로 동점자인 상황을 걸러내주는게 point word < best 라는 알파벳 비교도 포인트임

            best = word
            best_count = count
    return best