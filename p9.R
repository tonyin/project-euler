# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

SUM = 1000

p9 = function (x) {
  
  a_limit = floor(SUM / 3)
  for (a in seq(1, a_limit)) {
    b_limit = floor((SUM - a) / 2)
    for (b in seq(a + 1, b_limit)) {
      c_limit = SUM - a - b
      for (c in seq(b + 1, c_limit)) {
        if (a^2 + b^2 != c^2) { next }
        if (a + b + c != 1000) { next }
        return (a * b * c)
      }
    }
  }
}

t = proc.time()
p9(SUM)
proc.time() - t
