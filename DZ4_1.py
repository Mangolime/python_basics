from sys import argv


def zp(through_put, pay_rate, bonus):
    return through_put * pay_rate + bonus


print(zp(*map(float, argv[1:])))
