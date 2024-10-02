arr = [5,3,4,5,8,9]
count =1
for i in range(0,len(arr)-1):
    if arr[i]<arr[i+1]:
        count +=1
print(count)