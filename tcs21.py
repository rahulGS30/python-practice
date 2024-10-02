a = [5,8,3,2,1,4]
max_lenght = 0
arr = set(a)
for i in arr:
    if i-1 not in arr:
        current_num = i
        current_lenght =1
        
        while current_num+1 in arr:
            current_num+=1
            current_lenght+=1
    max_lenght = max(max_lenght,current_lenght)
print(max_lenght)