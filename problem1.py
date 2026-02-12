# If we list all the natural numbers below 10 that are multiples of
# 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def calculate_three_or_five_multiple_sum(upper_bound):
    msum = 0
    for i in range(upper_bound):
        if check_multiple(i):
            msum += i
    return msum

def check_multiple(number):
    return number % 3 == 0 or number % 5 == 0

print('Upper bound 10:', calculate_three_or_five_multiple_sum(10))
print('Upper bound 1000:', calculate_three_or_five_multiple_sum(1000))
