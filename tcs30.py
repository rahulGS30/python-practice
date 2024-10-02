def check(n):
    one = 0
    two = 0
    five = (n-4)//5

    if ((n-5*five)%2)==0:
        one = 2
    else:
        one =1

    two = ((n-5*five-one))//2 
    
    print(five)
    print(two)
    print(one)

n = 10
check(n)