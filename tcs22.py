s="nayannamantenet"
n= len(s)
def palinedrome(s):
    return s==s[::-1]
for i in range(1,n):
    first_part = s[:i]
    if palinedrome(first_part):
        for j in range(i+1,n):
            sec_part = s[i:j]
            third_part=s[j:]
            if palinedrome(sec_part) and palinedrome(third_part):
                print(first_part)
                print(sec_part)
                print(third_part)
