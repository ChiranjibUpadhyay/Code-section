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

    '''
    Given a keypad as shown in diagram, and an N digit number. List all words which are possible by pressing these numbers.



Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line of each test case is N, N is the number of digits. The second line of each test case contains D[i], N number of digits.

Output:
Print all possible words from phone digits with single space in lower case.

Constraints:
1 <= T <= 10
1 <= N <= 10
2 <=  D[i] <= 9

Example:
Input:
1
3
2 3 4

Output:
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi
'''