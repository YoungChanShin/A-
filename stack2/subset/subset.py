#순열
def f(n,k):
    if n==k:
        print(p)
    else:
        for i in range(k):
            if u[i]==0: # 사용되지 않은 숫자
                u[i]=1
                p.append(A[i])
                f(n+1,k) # 다음 사용할 요소 탐색
                p.pop()
                u[i]=0 # 원상복귀

A=list(range(1,4))
p=[]
u=[0]*len(A)
f(0,len(A))