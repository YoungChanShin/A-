import sys
sys.stdin=open('input.txt')

di=[0,0,1,-1]
dj=[1,-1,0,0]

def dfs(si,sj):
    if d[si][sj]=='3':
        return 1
    d[si][sj]='1'
    for k in range(4):
        ni=si+di[k]
        nj=sj+dj[k]
        if d[ni][nj]!='1':
            if dfs(ni,nj):
                return 1
    return 0

ts=int(input())
for test_case in range(1,1+ts):
    N=int(input())
    d=[['1']*(N+2)]
    for _ in range(N):
        d.append(['1']+list(input())+['1'])
    d.append(['1']*(N+2))
    for i in range(1,N+1):
        for j in range(1,N+1):
            if d[i][j]=='2':
                si=i
                sj=j
    
    print('#{} {}'.format(test_case, dfs(si,sj)))
