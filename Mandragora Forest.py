t = int(input())
if 1<=t<=100000:
    while t:
        n = int(input())
        l = list(map(int,input().split()))
        l.sort()
        s,p = n,0
        m = 0 
        
        right_sum = sum(l)
        a = right_sum
        
        for i in range(1, n):
            right_sum -= l[i-1]
            p = (i+1)*right_sum
            a = max(a,p)
        
         
        # for i in range(n-1,-1,-1):
        #     m += l[i]
        #     p = m*s
        #     if p>a:
        #         a = p
        #     s-=1
        
        
        
        print(a)
        t-=1