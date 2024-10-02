def rotate(arr,k):
    a = len(arr)
    k = k%a
    return arr[-k:]+arr[:-k]
    


def check(arr,k):
    rotated = rotate(arr,k)
    return rotated
    

arr = list(map(int,input().split(" ")))
k = int(input())
print(check(arr,k))