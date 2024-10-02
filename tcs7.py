day = input()
days = int(input())
m = {
    "mon":6,"tue":5, "wed":4,"thur":3,"fri":2,"sat":1
}
if days-m[day[:3]] >= 1:
    ans = 1+ (days-m[day[:3]])//7
print(ans)

