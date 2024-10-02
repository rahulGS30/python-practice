def check(n,arr1):
    if n<4:
        return 0
    if arr1[0].isdigit():
        return 
    cap=0
    nu=0
    for i in range(n):
        if arr1[i]==" " or arr1=="/":
            return 0
        if arr1[i]>='A' and arr1[i]<='Z':
            cap+=1
        if arr1[i].isdigit():
            nu+=1
        if nu>=0 and cap>=0:
            return 1
        else:
            return 9
        
    return 0

arr ="Du4GiH3n7g8"
arr1 = list(arr)
n = len(arr1)
print(check(n,arr1))
