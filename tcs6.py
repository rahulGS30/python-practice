n = int(input())
binary = bin(n)[2:]
arr = [x for x in binary]
e = len(arr)
k= 1
k= k%e
toggle= arr[-k:] + arr[:-k]
print(arr)
print(int(''.join(map(str,toggle)),2))
