str = "bbbaaababa"
n =3
count =0
max_value =0
for i in range(len(str)):
    if i%n==0:
        max_value=max(count,max_value)
        count=0
    if str[i]=='a':
        count+=1
if count>max_value:
    max_value=count
print(max_value)