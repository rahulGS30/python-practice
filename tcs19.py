arr1 = [3,1,2]
char = ['G','E','K']
arr=[]

for j in range(len(arr1)):
    arr.append("")
print(arr)
for i in range(len(arr1)):
    k = arr1[i]
    print(k)
    arr[k-1]=char[i]

print(arr)
