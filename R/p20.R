# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

N = 100


f = function (x) {
  num = prod(as.bigz(1:x))
  return (sum(as.numeric(strsplit(as.character(num), '')[[1]])))
}

# Run the function and timings
t = proc.time()
# install.packages('gmp') # uncomment if package needed
library(gmp)
f(N)
proc.time() - t
