import sys
sys.stdin=open('input.txt')

ts=int(input())
for test_case in range(1,1+ts):
    N=int(input())
    d=[list(map(int,input().split())) for _ in range(N)]
    p=[]
    for i in range(N):
        for j in range(N):
            if d[i][j]:
                d,a,b=measure(d,i,j) #b는 행의 길이
                p.append([a,b])
    for i in range(len(p)-1):
        for j in range(len(p)-1-i):
            if p[j][0]*p[j][1]>p[j+1][0]*p[j+1][1]:
                p[j], p[j+1]=p[j+1], p[j]
            if p[j][0]*p[j][1]==p[j+1][0]*p[j+1][1]:
                if p[j][1]>p[j+1][1]:
                    p[j], p[j + 1] = p[j + 1], p[j]
    ret='#{} '.format(test_case)
    for i in p:
        ret+=i[0]+' '
        ret+=i[1]+' '
    print(ret[:-1])