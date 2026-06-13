def averageScores(filename):
    try:
        txtfile = open(filename, 'r')
    except:
        return {}
    else:
        res_dict = {}
        for line in txtfile:
            if len(line.split(',')) != 2:
                continue
            else:
                name, score = line.strip().split(',')
                try:
                    score = float(score)
                except:
                    continue
                else:
                    res_dict[name] = res_dict.get(name, []) + [score]
        for name, score_list in res_dict.items():
            res_dict[name] = sum(score_list) / len(score_list)
        txtfile.close()
        return res_dict

print(averageScores('test.txt'))