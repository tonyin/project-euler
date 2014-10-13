# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

NUMBERS = 20

factorize = function (x) {
  for (i in 2:x) {
    if (x %% i == 0) {
      return (i)
    }
  }
}

p5 = function (x) {
  
  factors = list()
  
  for (i in 2:x) {
    
    n = i
    n_factors = list()
    while (n != 1) {
      f = factorize(n)
      if (is.null(n_factors[f][[1]])) {
        n_factors[f] = 1
      }
      else {
        n_factors[[f]] = n_factors[[f]] + 1
      }
      n = n/f
    }
    
    for (f in 2:length(n_factors)) {
      if (!is.null(n_factors[f][[1]])) {
        if (is.null(factors[f][[1]])) {
          factors[[f]] = n_factors[[f]]
        }
        else if (n_factors[[f]] > factors[[f]]) {
          factors[[f]] = n_factors[[f]]
        }
      }
    }
    
  }
  
  answer = 1
  for (i in 2:length(factors)) {
    if (!is.null(factors[i][[1]])) {
      answer = answer * i ^ (factors[[i]][[1]])
    }
  }
  
  return (answer)
}

t = proc.time()
p5(NUMBERS)
proc.time() - t