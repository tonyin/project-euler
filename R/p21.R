# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

N = 10000 - 1

find_factor = function (x) {
  if (x <= 3) { return (x) }
  for (i in 2:sqrt(x)) {
    if (x %% i == 0) {
      return (i)
    }
  }
  return (x)
}

get_prime_factors = function (num) {
  factors = list()
  while (num != 1) {
    f = as.character(find_factor(num))
    num = num / as.integer(f)
    if (is.null(factors[f][[1]])) {
      factors[f][[1]] = 1
    }
    else {
      factors[f][[1]] = factors[f][[1]] + 1
    }
  }
  return (factors)
}

get_permutations = function (f) {
  
  base = as.numeric(names(f)[1])
  powers = f[[1]]
  factors = c()
  
  if (length(f) > 1) {
    nested_factors = get_permutations(f[-1])
    for (i in 0:powers) {
      for (j in 1:length(nested_factors)) {
        factors = c(factors, base ^ i * nested_factors[j])
      }
    }
    factors = unique(factors)
  }
  else {
    for (i in 0:powers) {
      factors = c(factors, base ^ i)
    }
  }
  
  return (factors)
}

f = function (num) {
  
  amicable = c()
  for (i in 2:num) {
    factors = get_prime_factors(i)
    sum_prop = sum(get_permutations(factors)) - i
    if (sum_prop == 1) { next }
    if (sum_prop == i) { next }
    if (i %in% amicable) { next }
    
    pair_factors = get_prime_factors(sum_prop)
    pair_sum_prop = sum(get_permutations(pair_factors)) - sum_prop
    if (pair_sum_prop == i) {
      amicable = c(amicable, i, sum_prop)
    }
  }
  
  return (sum(unique(amicable)))
}

# Run the function and timings
t = proc.time()
f(N)
proc.time() - t
