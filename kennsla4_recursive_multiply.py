def multiply(a, b):
    if b == 0 or a == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b - 1) 
    else: 
        return -a + multiply(a, b + 1)