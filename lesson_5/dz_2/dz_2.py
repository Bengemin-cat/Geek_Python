def odd_nums(n):
    return (value for value in range(1, n + 1, 2))


odd_nums_15 = odd_nums(15)
print(next(odd_nums_15))
print(next(odd_nums_15))