t=int(input())
while t:
    string=input()
    if(len(string)%2!=0):
        print('not balanced')
    else:
        stack=[]
        top='q'
        y='p'
        #size=len(stack)
        for x in string:
            if top=='(':
                y=')'
            elif top==')':
                y='('
            elif top=='{':
                y='}'
            elif top=='}':
                y='{'
            elif top=='[':
                y=']'
            elif top==']':
                y='['
            if x==y:
                stack.pop()
                #size=size-1
                size=len(stack)
                if(size==0):
                    top='q'
                    y='p'
                else:
                    top=stack[size-1]
            else:
                stack.append(x)
                top=x
        if len(stack)==0:
            print('balanced')
        else:
            print('not balanced')
    t=t-1
