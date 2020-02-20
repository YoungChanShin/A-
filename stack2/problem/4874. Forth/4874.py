import sys
sys.stdin=open('input.txt')

def calc(a,i,b):
    a=int(a)
    b=int(b)
    if i=='+':
        return a+b
    if i=='-':
        return a-b
    if i=='*':
        return a*b
    if i=='/':
        return a//b

ts=int(input())
for test_case in range(1,1+ts):
    d=input().split()
    stack=[]
    flag=False
    for i in d:
        if not flag:
            if i=='.':
                if len(stack)!=1:
                    print('#{} {}'.format(test_case, 'error'))
                else:
                    ret=stack.pop()
                    print('#{} {}'.format(test_case, ret))
            elif i not in ['+','-','*','/','.']:
                stack.append(i)
            elif i in ['+','-','*','/']:
                if len(stack)>=2:
                    b=stack.pop()
                    a=stack.pop()
                    ret=calc(a,i,b)
                    stack.append(ret)
                else:
                    print('#{} {}'.format(test_case, 'error'))
                    flag=True
                    continue

                