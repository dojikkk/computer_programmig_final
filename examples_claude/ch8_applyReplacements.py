def applyReplacements(rules_filename, text_filename):
    try:
        rules = open(rules_filename, 'r')
        texts = open(text_filename, 'r')
        rule = {}
        for line in rules:
            parts = line.strip().split(',')
            if len(parts) != 2:
                continue
            a, b = parts
            rule[a] = b
        words = []
        for line in texts:
            words += line.split()
        res = []
        for word in words:
            if word in rule:
                res.append(rule[word])
            else:
                res.append(word)
        rules.close()
        texts.close()
        return ' '.join(res)
    except OSError:
        return ''