# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 21000?

N = 1000 # needs options(scipen = 999) for large numbers

f = function (x) {
  
  return (sum(as.numeric(strsplit(as.character(2^x), '')[[1]])))

}

# Run the function and timings
t = proc.time()
f(N)
proc.time() - t
