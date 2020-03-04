def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


print("###############################################")

def factorial(n):
    result = 1
    for x in range(1,n):
        result = x * result
    return result

for n in range(1,10):
    print(n, factorial(n+1))
