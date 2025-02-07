def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    n_half = n // 2

    high_x, low_x = divmod(x, 10**n_half)
    high_y, low_y = divmod(y, 10**n_half)

    z0 = karatsuba(low_x, low_y)
    z2 = karatsuba(high_x, high_y)
    z1 = karatsuba(low_x + high_x, low_y + high_y) - z2 - z0

    return z2 * 10**(2 * n_half) + z1 * 10**n_half + z0

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

product = karatsuba(x, y)

print(f"Product: {product}")
