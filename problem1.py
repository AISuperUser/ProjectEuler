# If we list all the natural numbers below 10 that are multiples of
# 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def calculate_three_or_five_multiple_sum(target):
    msum = 0
    for i in range(target):
        if check_multiple(i):
            msum += i
    return msum

def check_multiple(number):
    return number % 3 == 0 or number % 5 == 0

# way more efficient - may be used for larger targets
def calculate_three_or_five_multiple_improved(target):
    return sum_divisible_by(target, 3) + sum_divisible_by(target, 5) - sum_divisible_by(target, 15)

def sum_divisible_by(target, n):
    p = (target - 1) // n # // is integer division!
    return n * p * (p + 1) // 2


print('Upper bound 10:', calculate_three_or_five_multiple_sum(10))
print(calculate_three_or_five_multiple_improved(10))
print('Upper bound 1000:', calculate_three_or_five_multiple_sum(1000))
print(calculate_three_or_five_multiple_improved(1000))
