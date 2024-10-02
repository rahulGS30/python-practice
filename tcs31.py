def find_remainder_simple(str_num, k):
    # Convert the string to an integer
    num = int(str_num)
    
    # Find the remainder when num is divided by k
    remainder = num % k
    
    return remainder

# Test cases
print(find_remainder_simple("2345434534665", 6))  # Output: 3
print(find_remainder_simple("23454345346653434454543", 3))  # Output: 0
def find_remainder(str_num, k):
    remainder = 0
    
    for digit in str_num:
        remainder = (remainder * 10 + int(digit)) % k
    
    return remainder

# Test cases
print(find_remainder("2345434534665", 6))  # Output: 3
print(find_remainder("23454345346653434454543", 3))  # Output: 0
