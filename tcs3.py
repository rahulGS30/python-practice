n = int(input())
arr = list(map(int,input().split(" ")))
k = int(input())
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

def check(x,y,n):
    arr[x-1]=y
    ans=1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            ans+=1 
    return ans
    
print(check(x1,y1,n))
print(check(x2,y2,n))