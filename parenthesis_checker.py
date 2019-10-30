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


'''
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced
'''