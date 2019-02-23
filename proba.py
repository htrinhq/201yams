from math import factorial

def binomiale(x: int, y: int) -> float:
    """Get the binomial law between two values."""
    return (pow(1/6, y) * pow(5/6, x - y) * (factorial(x) / (factorial(y) *
    factorial(x - y))))


def proba(how_many: int, ref: int, list: [int]) -> float:
    """Get the final probability with a ref nb and a count nb"""
    occur = list.count(int(ref))
    res = 0
    if occur >= how_many:
        return 1
    for i in range(how_many - occur, 5 - occur + 1):
        res = res + binomiale(5 - occur, i)
    return res
