class ScoreList(list):
    def average(self):
        if not self or any(not isinstance(x, (int, float)) for x in self):
            raise ValueError
        return sum(self) / len(self)
    
    def passed(self, cutoff):
        res = ScoreList()
        for x in self:
            if x >= cutoff:
                res.append(x)
        return res
    
    def bumped(self, points):
        res = ScoreList()
        for x in self:
            res.append(x + points)
        return res


"""
def passed(self, cutoff):
    return ScoreList(x for x in self if x >= cutoff)
def bumped(self, points):
    return ScoreList(x + points for x in self)
"""