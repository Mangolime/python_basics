a, b = float(input()), float(input())
n_day = 1
cur_length = a
while cur_length < b:
    cur_length *= 1.1
    n_day += 1
print(n_day)
