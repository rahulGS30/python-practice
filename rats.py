def calculate(r,units,n,arr):
    if arr is None or n==0:
        return -1
    totalfood = r*units
    foodreq=0
    for i in range(n):
        foodreq += arr[i]
        if foodreq >= totalfood:
            return i+1
    return 0

r=int(input("enter the no.of: "))
units =  int(input("enter units of food required: "))
n = int(input("enter the no.of elements: "))
arr = list(map(int,input("enter elements: ").split()))
print(calculate(r,units,n,arr))