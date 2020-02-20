import sys
sys.stdin=open('input.txt')

def find_max_val(d):
    print('호출!')
    N=len(d)
    i=0
    if d[0]=='-':
        i=1
    while '0'<=d[i]<='9':
        i+=1
        if i==N:
            return int(d[:i])
    accum=d[:i]

    #i 다음의 연산자에 괄호 없이 계산하는 경우
    if N>=i+2:
        if N==i+2:
            ret1=eval(d)
        else:
            new_d=str(eval(d[:i+2])) + d[i+2:]
            ret1=find_max_val(new_d)
            # ret1=eval(str(eval(str(accum) + d[i:i+2])) + d[i+2] + str(find_max_val(d[i+3:])))
    
    #i 다음의 연산자에 괄호를 추가해 계산하는 경우
    if N>=i+4:
        if N==i+4:
            ret2=eval(str(accum) + d[i] + str(eval(d[i+1:])))
        else:
            new_d=str(eval(str(accum) + d[i] + str(eval(d[i+1:i+4]))))+d[i+4:]
            ret2=find_max_val(new_d)
            # ret2=eval(str(eval(str(accum) + d[i] + str(eval(d[i+1:i+4]))))+d[i+4]+ str(find_max_val(d[i+5:])))
        return max(ret1,ret2)
    return ret1

ts=int(input())
for test_case in range(ts):
    N=int(input())
    d=input()
    print(find_max_val(d))