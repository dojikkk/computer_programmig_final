def countAllLetters(line):
    line = line.lower()
    box = [0] * 26              # ← 26칸짜리 리스트로 알파벳 개수 셈
    res = []
    for i in line:
        if i.isalpha():
            box[ord(i) - ord('a')] += 1   # 'a'=0번칸, 'b'=1번칸...
    for index, k in enumerate(box):
        if k != 0:
            res.append((chr(index + ord('a')), k))
    return res

def countAllLetters_dict(line):
    line = line.lower()
    freq = {}
    for ch in line:
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1   # ord 계산 없이 글자를 바로 키로!
    return list(freq.items())

"""
"""