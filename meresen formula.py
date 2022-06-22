import math
def lucas_lehmer_series(p)
 ll_seq = [4]
  if p>2:
    for i inrange(1,(p-2)+1):
      n_i=((ll_seq[i-1])**2-2) % ((2**p)-1)
      ll_seq.append(n_i)
      return ll_seq
    def is_prime(number):
      if number <= 1 or (number >2 and number % 2 == 0):
        return false
      
      for factor in range(2, int(math.sqrt(number))+1:
                          if number%factor == 0:
                          retrun false
                          return true
                          defll_prime(p)
                          if lucas_lehmer_series(p)[-1] == 0:
                     retrun true
                          return false
