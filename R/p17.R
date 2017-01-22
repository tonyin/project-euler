# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

N = 1000 # supports up to 9999

f = function (x) {
  
  singles = c('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
  teens = c('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
  names(teens) = c(10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
  doubles = c('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
  names(doubles) = c(20, 30, 40, 50, 60, 70, 80, 90)
  
  word_lengths = c()
  
  for (i in 1:9) {
    word_lengths[i] = nchar(singles[i])
  }
  if (x > 9) {
    for (i in 10:19) {
      word_lengths[i] = nchar(teens[as.character(i)])
    }
  }
  if (x > 20) {
    for (i in 2:9) {
      for (j in 0:9) {
        if (j == 0) {
          word_lengths[i * 10] = nchar(doubles[as.character(i * 10)])
        }
        else {
          word_lengths[i * 10 + j] =
            word_lengths[i * 10] +
            word_lengths[j]
        }
      }
    }
  }
  if (x > 99) {
    for (i in 1:9) {
      for (j in 0:9) {
        for (k in 0:9) {
          if (j * 10 + k == 0) {
            word_lengths[i * 100] = word_lengths[i] + nchar('hundred')
          }
          else {
            word_lengths[i * 100 + j * 10 + k] =
            word_lengths[i * 100] + nchar('and') +
            word_lengths[j * 10 + k]
          }
        }
      }
    }
  }
  if (x > 999) {
    for (i in 1:9) {
      for (j in 0:9) {
        for (k in 0:9) {
          for (l in 0:9) {
            if (j * 100 + k * 10 + l == 0) {
              word_lengths[i * 1000] = word_lengths[i] + nchar('thousand')
            }
            else {
              word_lengths[i * 1000 + j * 100 + k * 10 + l] =
                word_lengths[i * 1000] +
                word_lengths[j * 100 + k * 10 + l]
            }
          }
        }
      }
    }
  }
  
  return (sum(word_lengths[1:x]))
    
}

# Run the function and timings
t = proc.time()
f(N)
proc.time() - t
