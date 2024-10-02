n = int(input())
r = int(input())
def sum_of(n):
    return sum(int(digit) for digit in str(n))
def check(n,r):
    sum_digits = sum_of(n)
    total_sum = sum_digits*r
    while total_sum >= 10:
        total_sum = sum_of(total_sum)
    return total_sum
print(check(n,r))