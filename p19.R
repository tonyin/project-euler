# You are given the following information, but you may prefer to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

START = 1900
END = 2000


f = function (start, end) {
  
  months = c(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
  
  firsts = logical()
  counter = 1
  
  for (i in start:end) {
    for (j in 1:12) {
      firsts[counter] = TRUE
      if (j == 2) {
        if (i %% 4 == 0) {
          if (i %% 100 == 0) {
            if (i %% 400 == 0) { counter = counter + 1 }
          }
          else {
            counter = counter + 1
          }
        }
      }
      counter = counter + months[j]
    }
  }
  
  sunday_firsts = 0
  firsts = which(firsts)
  for (i in seq_along(firsts)) {
    if (i <= 12) { next } # skip 1900
    if (firsts[i] %% 7 == 0) { # 1 == Monday, 7 == Sunday, +7 == Sunday thereafter
      sunday_firsts = sunday_firsts + 1
    }
  }
  
  return (sunday_firsts)
}

# Run the function and timings
t = proc.time()
f(START, END)
proc.time() - t
