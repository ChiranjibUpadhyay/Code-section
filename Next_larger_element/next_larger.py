t=int(input())
while t:
    n=int(input())
    list1=list(map(int,input().split()))
    final=[0 for i in range(n)]
    stack=[]
    stack.append(0)
    for i,x in enumerate(list1[1:]):
        appended=False
        while len(stack)!=0:
            if list1[stack[len(stack)-1]]<x:
                top=stack.pop()
                final[top]=x
            else:
                stack.append(i+1)
                appended=True
                break
        if appended!=True:
            stack.append(i+1)
    size=len(stack)
    if size!=0:
        while size!=0:
            top=stack.pop()
            final[top]=-1
            size=size-1
    print(*final)
    t=t-1
