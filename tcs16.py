t = 5
num1 = [7,0,5,1,3]
num2 = [1,2,1,3,4]
current =0
max=0
for i in range(t):
    current = current+num1[i]-num2[i]
    if current>max:
        max=current
print(max)