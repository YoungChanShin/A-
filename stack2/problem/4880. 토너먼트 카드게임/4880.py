import sys
sys.stdin=open('input.txt')

def rps(a, b):
    num1=d[a]
    num2=d[b]
    if num1==num2:
        return a
    if num1==1:
        if num2==2:
            return b
        if num2==3:
            return a
    if num1==2:
        if num2==1:
            return a
        if num2==3:
            return b
    if num1==3:
        if num1==1:
            return b
        if num1==2:
            return a
        

def paly(i,j):
    if j-i<=1:
        return rps(i,j)
    a=paly(i,(i+j)//2)
    b=paly((i+j)//2+1,j)
    return rps(a,b)

ts=int(input())
for test_case in range(1,1+ts):
    people=int(input())
    d=list(map(int,input().split()))
    print('#{} {}'.format(test_case,(paly(0,people-1)+1)))