t=int(input())
while t:
    n=int(input())
    list1=[]
    minm=99999999
    list1=list(map(int,input().split()))
    list1.sort()
    k=int(input())
    for i in range(n-k+1):
        j=i+k-1
        p=abs(list1[j]-list1[i])
        if minm>p:
            minm=p
    print(minm)
    t=t-1
