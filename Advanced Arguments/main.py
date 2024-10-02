def _sum(*args):
    n_sum = 0
    for n in args:
        n_sum = n_sum + n
    return n_sum


print(_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
