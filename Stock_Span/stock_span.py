t=int(input())
while t:
    n=int(input())
    dict1={}
    stack=[]
    final=[]
    list1=list(map(int,input().split()))
    for i,x in enumerate(list1):
        dict1[i]=1
        final.append(1)
    stack.append(0)
    for ind,val in enumerate(list1[1:]):
        size=len(stack)
        while size!=0:
            if list1[stack[size-1]]<= val:
                pre=stack.pop()
                size=size-1
                dict1[ind+1]=dict1[ind+1]+dict1[pre]
            else:
                break
        final[ind+1]=dict1[ind+1]
        stack.append(ind+1)
    print(*final)
    t=t-1
