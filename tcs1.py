N = int(input())
K = int(input())
arr = list(map(int,input().split(" ")))
def check(n,k,arr):
    start,end,current_sum= 0,0,0
    result_start,result_end = 0 , float('inf')
    while end<n:
        current_sum += arr[end]
        while current_sum>k:
            current_sum -= 0
            start +=1
        if current_sum ==k:
            return(start+1,end+1)
            
        end +=1
        
    if restart_end==float('inf'):
        return "no solution"
    else:
        print(result_start+1,restart_end+1)
            
    
print(check(N,K,arr))