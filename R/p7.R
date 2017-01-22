# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

NUMBER = 10001

next_prime = function (x) {
  if (x == 1) { return (2) }
  
  repeat {
    is_prime = TRUE
    x = x + 1
    for (i in 2:sqrt(x)) {
      if (x %% i == 0) {
        is_prime = FALSE
        break
      }
    }
    if (is_prime) { return (x) }
  }
}

p7 = function (x) {
  
  p = 0
  last = 1
  while (p < x) {
    last = next_prime(last)
    p = p + 1
  }
  
  return (last)
}

t = proc.time()
p7(NUMBER)
proc.time() - t