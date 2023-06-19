def prime_factors(x: int) -> list[int]:
    res = []
    for factor in range(2, x):

        if x & factor == 0:
            res.append(factor)
        else:
            pass

    return res


print(prime_factors(8))
