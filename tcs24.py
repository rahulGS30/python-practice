r = int(input())
c = int(input())
matrix = []
for i in range(r):
    row = list(map(int,input().split(" ")))
    matrix.append(row)
max_val = 0
max_index = -1
for i in range(r):
    count = sum(matrix[i])
    if count > max_val:
        max_val= count
        max_index +=1
print(max_index+1)