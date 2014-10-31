# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# 
# How many such routes are there through a 20×20 grid?

N = 20

f = function (x) {
  
  return (factorial(2 * x) / factorial(x)^2)

}

# Run the function and timings
t = proc.time()
f(N)
proc.time() - t
