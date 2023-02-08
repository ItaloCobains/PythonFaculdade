def rec(n):
     if n < 2:
          return rec(n - 1)


print(rec(1))