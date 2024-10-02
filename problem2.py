'''Problem Statement – Ritik wants a magic board, which displays a character for a 
corresponding number for his science project. Help him to develop such an 
application.
For example when the digits 65,66,67,68 are entered, the alphabet ABCD are to be 
displayed.
[Assume the number of inputs should be always 4 ]
Sample Input 1:
Enter the digits:65666768
Sample Output 1:
65-A
66-B
67-C
68-D'''
import textwrap

num = "65666769"
arr = textwrap.wrap(num,2)
arr = [int(n) for n in arr]
print(arr)
for i in range(0,len(arr)):
    if arr[i]==65:
        print(f"{arr[i]}-A")
    if arr[i]==66:
        print(f"{arr[i]}-B")
    if arr[i]==67:
        print(f"{arr[i]}-C")
    if arr[i]==68:
        print(f"{arr[i]}-D")