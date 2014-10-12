# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

DIGITS = 3

check_palindrome = function(x) {
  number = strsplit(as.character(x), "")[[1]]
  digits = length(number)
  if (digits == 1) { return (TRUE) }
  
  if (digits %% 2 == 0) {
    for (i in 1:(digits/2)) {
      if (number[i] != number[digits+1-i]) { return (FALSE) }
    }
  }
  else {
    for (i in 1:((digits-1)/2)) {
      if (number[i] != number[digits+1-i]) { return (FALSE) }
    }
  }
  
  return (TRUE)
}

p4 = function(x) {
  n_max = 10^x
  answer = 0
  
  for (i in 1:n_max) {
    for (j in 1:i) {
      n_prod = (n_max-i) * (n_max-j)
      if (check_palindrome(n_prod)) {
        if (n_prod > answer) {
          answer = n_prod
        }
      }
    }
  }
  
  return (answer)
}

t = proc.time()
p4(DIGITS)
proc.time() - t