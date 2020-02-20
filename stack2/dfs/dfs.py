import sys
sys.stdin=open('input.txt')
def visit(i):
    print(i)

def dfs1(n,V):
    visited[n]=1
    visit(n)
    for i in range(1,1+V):
        if adj[n][i]==1 and visited[i]==0:
            dfs1(i,V)
def dfs2(n,V):
    stack=[]
    stack.append(n)
    visited[n]=1
    while stack:
        n=stack.pop()
        visit(n)
        for i in range(1, V+1):
            if adj[n][i]==1 and visited[i]==0:
                stack.append(i)
                visited[i]=1


V,E=map(int, input().split())
edge=list(map(int, input().split()))
adj=[[0]*(V+1) for _ in range(V+1)]
visited=[0]*(V+1)
for i in range(E):
    n1=edge[2*i]
    n2=edge[2*i+1]
    adj[n1][n2]=1
dfs2(4,V)