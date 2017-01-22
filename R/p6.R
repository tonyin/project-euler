# The sum of the squares of the first ten natural numbers is,
# 
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

NUMBERS = 100

sum_of_squares = function (x) {
  return (x * (x + 1) * (2 * x + 1) / 6)
}
square_of_sum = function (x) {
  return ((x * (x + 1) / 2) ^ 2)
}

p6 = function (x) {
  return (abs(sum_of_squares(x) - square_of_sum(x)))
}

t = proc.time()
p6(NUMBERS)
proc.time() - t