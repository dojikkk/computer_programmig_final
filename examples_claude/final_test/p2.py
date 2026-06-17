def averageScores(records):
    """
    records: list of (name, score) tuples. A name may appear multiple times.
    Returns a dict mapping each name to its average score (float).

    Example:
        averageScores([("Ana", 80), ("Ben", 60), ("Ana", 100)])
        -> {"Ana": 90.0, "Ben": 60.0}
    """
    # TODO
    res = {}
    for a, b in records:
        res[a] = res.get(a, []) + [b]
    return {a : sum(b) / len(b) for a, b in res.items()}