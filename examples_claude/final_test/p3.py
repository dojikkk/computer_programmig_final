def processGrades(in_filename, out_filename):
    try:
        f_in = open(in_filename, 'r')
    except OSError:
        print("Could not open input file")   # 명세: 에러 메시지 출력!
        return None

    f_out = open(out_filename, 'w')
    count = 0
    for line in f_in:
        parts = line.split()
        try:
            name = parts[0]
            score = int(parts[1])   # 점수 없으면 IndexError, 숫자 아니면 ValueError
        except (IndexError, ValueError):
            continue                # 손상된 줄 스킵
        count += 1
        result = "PASS" if score >= 60 else "FAIL"
        f_out.write('{}: {}\n'.format(name, result))   # 명세 포맷 + \n!

    f_in.close()
    f_out.close()
    return count

"""
line = line.split() 

split()은 항상 문자열 리스트를 돌려줘.
그래서 line[1]은 영원히 str이고, isinstance(line[1], int)는 언제나 False → 전부 스킵.
에러 주의하기

if len(line) != 2 or not isinstance(line[1], int):
    continue
"""