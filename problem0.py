# A number is a perfect square, or a square number, if it is the square of a positive integer.
# For example, 25 is a square number because 5^2 = 5 * 5 = 25; it is also an odd square.
# The first 5 square numbers are: 1, 4, 9, 16, 25 , and the sum of the odd squares is
# 1 + 9 + 25 = 35
# Among the first 101 thousand square numbers, what is the sum of all the odd squares?
def calculate_odd_square_sum(square_count):
    square_sum = 0
    for i in range(1, square_count + 1, 2):
        square_sum += i ** 2
    return square_sum

def calculate_odd_square_sum_improved(square_count):
    # Only sum odd perfect squares, i.e., squares of odd numbers
    return sum(i**2 for i in range(1, square_count + 1, 2))

print(calculate_odd_square_sum(5))
print(calculate_odd_square_sum_improved(5))
print(calculate_odd_square_sum(101_000))
print(calculate_odd_square_sum_improved(101_000))
