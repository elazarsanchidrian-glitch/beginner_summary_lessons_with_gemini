import math
from fractions import Fraction

#divide two numbers
division = 5/2
print("printing division of 5/2 = ", division)

#without remainder nor float
division_without_remainder = 5//2
print("printing division without remainder of 5//2 = ", division_without_remainder)

#pedmas and bodmas order of operations
without_parentheses = 5 + 2 * 3
with_parentheses = (5 + 2) * 3
print(" printing without_parentheses of 5 + 2 * 3 = ", without_parentheses)
print(" printing with parentheses of (5 + 2) * 3 = ", with_parentheses)

#exponents
exponent = 2 ** 3
print(" printing exponent of 2 ** 3 = ", exponent)

#exponent equations
exponent_equation = 2 ** 3 + 5 * 2
print(" printing exponent equation of 2 ** 3 + 5 * 2 = ", exponent_equation)

#with parentheses exponent equations
exponent_equation_with_parentheses = (2 ** 3) + (5 * 2)
print(" printing exponent equation with parentheses of (2 ** 3) + (5 * 2) = ", exponent_equation_with_parentheses)

# Without parentheses: exponent applies only to 2
without_parentheses_exponent = 2**3 + 5  # (2 ** 3) + 5 = 8 + 5 = 13
print(" printing without parentheses exponent of 2**3 + 5 = ", without_parentheses_exponent)

# With parentheses: addition happens before the exponent
with_parentheses_exponent = 2 ** (3 + 5)  # 2 ** 8 = 256
print(" printing with parentheses exponent of 2 ** (3 + 5) = ", with_parentheses_exponent)

#fractions adding plus
fraction_calculation = (1/2) + (1/2)
print(" printing fraction calculation of (1/2) + (1/2) = ", fraction_calculation)

#fraction result whole number plus or adding
fraction_result_whole = Fraction(1, 2) + Fraction(1, 2)
print(" printing fraction result whole of Fraction(1, 2) + Fraction(1, 2) = ", fraction_result_whole)

#dividing fractions
dividing_fractions = (1/2) / (1/4)
print(" printing dividing fractions of (1/2) / (1/4) = ", dividing_fractions)

#dividing fractions result whole number
dividing_fractions_whole = Fraction(1, 2) / Fraction(1,4)
print(" printing dividing fractions whole of Fraction(1, 2) / Fraction(1,4) = ", dividing_fractions_whole)

#multiplying fractions
multiplying_fractions = (1/2) * (1/4)
print(" printing multiplying fractions of (1/2) * (1/4) = ", multiplying_fractions)

#multiplying fractions result whole number
multiplying_fractions_whole = Fraction(1, 2) * Fraction(1,4)
print(" printing multiplying fractions whole of Fraction(1, 2) * Fraction(1,4) = ", multiplying_fractions_whole)

#big math equation using pedmas and bodmas order of operations
big_math_equation = (5 * 2) + (3 * 2) / (6 + 2) * (2 + 3)
print(" printing big math equation of (5 * 2) + (3 * 2) / (6 + 2) * (2 + 3) = ", big_math_equation)

#make it a whole int number
big_math_equation_whole = int(big_math_equation)
print(" printing big math equation whole of int((5 * 2) + (3 * 2) / (6 + 2) * (2 + 3)) = ", big_math_equation_whole)

#make it round
big_math_equation_rounded = round(big_math_equation)
print(" printing big math equation rounded of round((5 * 2) + (3 * 2) / (6 + 2) * (2 + 3)) = ", big_math_equation_rounded)