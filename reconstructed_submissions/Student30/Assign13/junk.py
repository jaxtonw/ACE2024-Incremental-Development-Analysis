# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
# Assignment ??

def aggienacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (aggienacci(n-3) + aggienacci(n-2)) / 
ggienacci(n - 1)

print(aggienacci(9)))
