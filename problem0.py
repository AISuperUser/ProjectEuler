# A number is a perfect square, or a square number, if it is the square of a positive integer.
# For example, 25 is a square number because 5^2 = 5 * 5 = 25; it is also an odd square.
# The first 5 square numbers are: 1, 4, 9, 16, 25 , and the sum of the odd squares is
# 1 + 9 + 25 = 35
# Among the first 101 thousand square numbers, what is the sum of all the odd squares?
class Problem0:
  def calculate_odd_square_sum(square_count):
    square_sum = 0
    for i in range(0, square_count + 1):
        i_square = i ** 2
        if i_square % 2 == 1:
            square_sum += i_square
    return square_sum

print(Problem0.calculate_odd_square_sum(101000))