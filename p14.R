# The following iterative sequence is defined for the set of positive integers:
#   
#   n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
#   
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

N = 1000000

f = function (start) {
  
  num = start
  terms = 1
  repeat {
    if (num <= 1) {
      return (terms)
    }
    else if (num %% 2 == 0) {
      num = num / 2
      terms = terms + 1
    }
    else {
      num = 3 * num + 1
      terms = terms + 1
    }
  }

}
g = function (x) {
  num = 1
  most_terms = 1
  for (i in 1:x) {
    terms = f(x - i)
    if (terms > most_terms) {
      most_terms = terms
      num = x - i
      print (num)
    }
  }
  return (num)
}

# Run the function and timings
t = proc.time()
g(N)
proc.time() - t
