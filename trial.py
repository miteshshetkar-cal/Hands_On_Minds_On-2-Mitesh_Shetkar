def solve():
    """Finds the numerator of the fraction immediately to the left of 3/7 
    in the sorted list of reduced proper fractions with d <= 1000000.
    """

    target_numerator = 3
    target_denominator = 7
    
    best_numerator = 0
    best_denominator = 1  # Initialize with 0/1 (smaller than any proper fraction)

    for denominator in range(2, 1000001):
        numerator = (target_numerator * denominator - 1) // target_denominator
        
        if numerator / denominator < target_numerator / target_denominator:
            if numerator * best_denominator > best_numerator * denominator:
                best_numerator = numerator
                best_denominator = denominator

    return best_numerator,best_denominator


result = solve()
print(result)

# def find_preceding_fraction(target_numerator, target_denominator, max_denominator):
#     left_numerator, left_denominator = 0, 1
#     right_numerator, right_denominator = target_numerator, target_denominator

#     while True:
#         mediant_numerator = left_numerator + right_numerator
#         mediant_denominator = left_denominator + right_denominator

#         if mediant_denominator > max_denominator:
#             return left_numerator, left_denominator  # Return the last valid fraction

#         if mediant_numerator * target_denominator < target_numerator * mediant_denominator:
#             left_numerator, left_denominator = mediant_numerator, mediant_denominator
#         else:
#             return left_numerator, left_denominator  # Found the preceding fraction

# # Find the fraction immediately to the left of 3/7 for d <= 1000000
# numerator, denominator = find_preceding_fraction(3, 7, 1000000)
# print(f"The fraction immediately to the left of 3/7 is {numerator}/{denominator}")