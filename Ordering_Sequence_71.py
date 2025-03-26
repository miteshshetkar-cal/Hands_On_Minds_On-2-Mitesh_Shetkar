
from math import gcd

def ordering_serquence(target_n, target_d, max_denominator):
    left_n, left_d = 0, 1
    right_n, right_d = 3, 7

    while True:
        mediant_n = left_n + right_n
        mediant_d = left_d + right_d

        common_divisor = gcd(mediant_n, mediant_d)
        mediant_n //= common_divisor
        mediant_d //= common_divisor

        if mediant_d > max_denominator:
            break

        if mediant_n * target_d < target_n * mediant_d:
            left_n, left_d = mediant_n, mediant_d
        else:
            right_n, right_d = mediant_n, mediant_d

    return left_n, left_d


# max_denominator = 8
max_denominator = 1000000
target_n, target_d = 3, 7

result_n, result_d = ordering_serquence(target_n, target_d, max_denominator)

print(f"Numerator of the fraction immediately to the left of 3/7: {result_n}/{result_d}")
