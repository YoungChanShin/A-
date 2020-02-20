import sys
sys.stdin = open("input.txt", 'r')
def find_max_val(oper_idx,accum,max_val):
    N=len(d)
    if oper_idx>=N-1:
        if max_val<accum:
            max_val=accum
        return max_val
    if d[oper_idx]=='+':
        ret1=find_max_val(oper_idx+2, accum+int(d[oper_idx+1]), max_val)
        if max_val<ret1:
            max_val=ret1
        if oper_idx<=N-4:
            ret2=find_max_val(oper_idx+4, accum+eval(d[oper_idx+1:oper_idx+4]), max_val)
            if max_val<ret2:
                max_val=ret2

    if d[oper_idx]=='-':
        ret1=find_max_val(oper_idx+2, accum-int(d[oper_idx+1]), max_val)
        if max_val<ret1:
            max_val=ret1
        if oper_idx<=N-4:
            ret2=find_max_val(oper_idx+4, accum-eval(d[oper_idx+1:oper_idx+4]), max_val)
            if max_val<ret2:
                max_val=ret2

    if d[oper_idx]=='*':
        ret1=find_max_val(oper_idx+2, accum*int(d[oper_idx+1]), max_val)
        if max_val<ret1:
            max_val=ret1
        if oper_idx<=N-4:
            ret2=find_max_val(oper_idx+4, accum*eval(d[oper_idx+1:oper_idx+4]), max_val)
            if max_val<ret2:
                max_val=ret2
    return max_val
ts=int(input())
for test_case in range(ts):
    N=int(input())
    d=input()
    max_val=-(2**31)+1
    print(find_max_val(1,int(d[0]),max_val))