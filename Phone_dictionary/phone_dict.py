def find_dot(x,y):
    list2=[]
    list2=[i+j for i in x for j in y ]
    return list2
t=int(input())
d={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
while t:
    n=int(input())
    list1=[]
    list1=list(map(int,input().split()))
    x=[]
    x=d[list1[0]]
    for y in list1[1:]:
        x=find_dot(x,d[y])
    print(*x)
    t=t-1
