import sys
sys.stdin=open('input.txt')

ts=int(input())
def dfs1(n,e,V):
    visited[n]=1
    if n==e:
        return True
    for i in range(1,1+V):
        if adj[n][i]==1 and visited[i]==0:
            if dfs1(i,e,V):
                return True
    return False

for test_case in range(1,1+ts):
    V,E=map(int, input().split())
    adj=[[0]*(V+1) for _ in range(V+1)]
    visited=[0]*(V+1)
    for _ in range(E):
        s,e=list(map(int, input().split()))
        adj[s][e]=1
    s,e=list(map(int, input().split()))
    if dfs1(s,e,V):
        print('#{} 1'.format(test_case))
        continue
    print('#{} 0'.format(test_case))