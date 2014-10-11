# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

NUM = 600851475143

check_sqrt = function(x) {
  if (sqrt(x) %% 1 == 0) {
    check_sqrt(sqrt(x))
  }
  else {
    check_incr(x)
  }
}

check_incr = function(x) {
  n = ceiling(sqrt(x))
  while (x %% n != 0) {
    n = n - 1
  }
  if (n == 1 | n == x) {
    return(x)
  }
  else {
    return(max(
      check_sqrt(n),
      check_sqrt(x/n)
    ))
  }
}

p3 = function(x) {
  if (x == 1) { return(x) }
  return(check_sqrt(x))
}

t = proc.time()
p3(NUM)
proc.time() - t
