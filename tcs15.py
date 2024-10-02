from collections import Counter
b = ['r','g','g','h','h','i','i']
count = Counter(b)
for i in count:
    if count[i]%2 !=0:
        print(i)
