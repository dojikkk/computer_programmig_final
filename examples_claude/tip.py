# tip.py
# A restaurant bill / tip calculator module.

DEFAULT_TIP_RATE = 0.2   # module-level constant


def tip_amount(bill, rate):
    """Return the tip for `bill` at the given `rate` (e.g. 0.2 means 20%)."""
    return bill * rate


def total_with_tip(bill, rate):
    """Return bill + tip. Constraint: REUSE tip_amount() — do not recompute."""
    return bill + tip_amount(bill, rate)


def per_person(total, people):
    """Return each person's equal share of `total`.
       Raise ValueError if people <= 0."""
    if people <= 0:
        raise ValueError
    return total / people
    # TODO  


if __name__ == "__main__":
    pass