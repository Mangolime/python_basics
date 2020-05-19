n = int(input())
n_rest = n
i = 10
max_digit = 0
while n_rest > 0:
    cur_digit = n_rest % 10
    if cur_digit > max_digit:
        max_digit = cur_digit
    n_rest //= 10
print(max_digit)
