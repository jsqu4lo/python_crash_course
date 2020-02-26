def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    n = 1
    for n in range(x):
      x = square(n)
      sum += x
    return sum

print(sum_squares(10)) # Should be 285
