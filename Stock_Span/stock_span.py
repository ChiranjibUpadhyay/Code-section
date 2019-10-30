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

    '''
    The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the size of the array. The second line of each test case contains N input C[i].

Output:
For each testcase, print the span values for all days.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 200
1 ≤ C[i] ≤ 800

Example:
Input:
2
7
100 80 60 70 60 75 85
6
10 4 5 90 120 80

Output:
1 1 1 2 1 4 6
1 1 2 4 5 1
'''