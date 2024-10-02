n = 8  # Input the number

# Initialize the product
p = 1

# While n is greater than 4, subtract 3 and multiply the product by 3
while n%3 != 0:
    n -= 2
    p *= 2
print(p*(3**(n//3)))
