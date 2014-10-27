# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

LIMIT = 2000000

p10 = function (x) {
  n = sapply(logical(x), function(x) x = TRUE)
  n[1] = FALSE
  
  for (i in 2:sqrt(x)) {
    if (n[i]) {
      n[seq_along(n) > i & seq_along(n) %% i == 0] = FALSE
    }
  }

  return (sum(as.numeric((which(n)))))
}

t = proc.time()
p10(LIMIT)
proc.time() - t
