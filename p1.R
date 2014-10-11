# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

LIMIT = 1000

p1 = function(x) {
  return(
    sum(seq(0, x-1, 3)) + sum(seq(0, x-1, 5)) - sum(seq(0, x-1, 15))
  )
}

t = proc.time()
p1(LIMIT)
proc.time() - t