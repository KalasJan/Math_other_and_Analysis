# YT - Mind your decision
# The russian doll
# https://www.youtube.com/watch?v=UlZSFIXsvD8

# f(n) = n - 3 if n > = 1000
# f(n) = f(f(n+5)) if n < 1000
# f(84) = ?

def f(n):
    while n < 1000:
        return f(f(n+5))
    else:
        return n - 3
print (f(84))