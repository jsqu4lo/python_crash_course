def sum_divisors(n):
  m = 1
  sum = 0
  # Return the sum of all divisors of n, not including n
  while m < n:
    if n%m == 0:
      sum = sum + m
    m += 1
  return sum

print(sum_divisors(6)) # Should be 6 (sum of 1+2+3)
print(sum_divisors(12)) # Should be 16 (sum of 1+2+3+4+6)

