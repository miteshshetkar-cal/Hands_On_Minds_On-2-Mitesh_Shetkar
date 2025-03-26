# # def is_triangle_number(num):
# #     """Checks if a number is a triangle number (integer-based)."""
# #     if num < 0:
# #         return False
# #     triangle_sum = 0
# #     k = 1
# #     while triangle_sum < num:
# #         triangle_sum += k
# #         if triangle_sum == num:
# #             return True
# #         k += 1
# #     return False

# # def calculate_m(n):
# #     """Calculates M(n) = n(n + 2)."""
# #     return n * (n + 2)

# # def generate_sequence(num_terms):
# #     """Generates the sequence of n values where M(n) is a triangle number."""
# #     sequence = []
# #     n = 1
# #     count = 0 # add count to make sure the loop ends correctly.
# #     while count < num_terms:
# #         m_n = calculate_m(n)
# #         if is_triangle_number(m_n):
# #             sequence.append(n)
# #             count += 1
# #         n += 1
# #     return sequence

# # # Example: Find the 20th term
# # sequence = generate_sequence(20)
# # print(f"The 20th term is: {sequence[19]}")




# N = 40


# def gen_solution():
#     D = 8
#     base_sol = [(1, 1), (5, 2)]
#     a, b = 3, 1
#     for x, y in base_sol:
#         yield x, y
#     while True:
#         for i in range(len(base_sol)):
#             x, y = base_sol[i]
#             x, y = x * a + D * y * b, x * b + y * a
#             yield x, y
#         a, b = 3 * a + 8 * b, a + 3 * b


# ls = []
# for x, y in gen_solution():
#     if (x - 1) % 2 == 0 and (x - 1) // 2 > 0:
#         ls.append(y - 1)
#         if len(ls) == N:
#             break
# ans = sum(ls)
# print(ans)


import time
start_time = time.time()

def equationsolver(x, startx, starty, a, b, c, d, e, f):
    x1 = startx
    y1 = starty
    solutions = []
    while len(solutions) != x:
        xn = a*x1 + b*y1 + c
        yn = d*x1 + e*y1 + f
        if xn > 0:
            solutions.append(xn)
        x1 = xn
        y1 = yn
    return solutions

def compute(limit):
    solutions = equationsolver(40, 0, 0, 3, 2, 3, 4, 3, 5) + equationsolver(40, 0, -1, 3, 2, 3, 4, 3, 5)
    return sum(sorted(list(set(solutions)))[:limit])

if __name__ == "__main__":
    print(compute(40))
    print("--- %s seconds ---" % (time.time() - start_time))