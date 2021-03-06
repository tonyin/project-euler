# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#   
#   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

LIMIT = 4000000

p2 = function(x) {
  prev = 1
  curr = 2
  total = 0
  
  while (curr < LIMIT) {
    if (curr %% 2 == 0) {
      total = total + curr
    }
    tmp = prev + curr
    prev = curr
    curr = tmp
  }

  return(total)
}

t = proc.time()
p2(LIMIT)
proc.time() - t
