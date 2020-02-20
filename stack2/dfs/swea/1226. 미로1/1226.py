import sys
sys.stdin=open('input.txt')
di=[0,0,1,-1]
dj=[1,-1,0,0]

def find_sp_ep():
    si,sj,ei,ej=0,0,0,0
    for i in range(16):
        for j in range(16):
            if data_list[i][j]=='2':
                si,sj=i,j
            if data_list[i][j]=='3':
                ei,ej=i,j
    return si,sj,ei,ej

# def dfs(si,sj,ei,ej):
#     stack=[]
#     for i in range(4):
#         if data_list[si+di[i]][sj+dj[i]]=='3':
#             return 1
#         if data_list[si+di[i]][sj+dj[i]]=='0':
#             stack.append((si+di[i],sj+dj[i]))
#             data_list[si+di[i]][sj+dj[i]]='1'

#     while stack:
#         new_i,new_j=stack.pop()
#         if dfs(new_i,new_j,ei,ej):
#             return 1
#     return 0
def dfs_ans(i,j):
    if data_list[i][j]=='3':
        return 1
    else:
        data_list[i][j]='1'
        for k in range(4):
            ni=i+di[k]
            nj=j+dj[k]
            if data_list[ni][nj]!='1':
                if dfs_ans(ni,nj):
                    return 1
    


for _ in range(10):
    test_case=int(input())
    data_list=[list(input()) for _ in range(16)]
    si,sj,ei,ej=find_sp_ep()
    # print('#{} {}'.format(test_case,dfs(si,sj,ei,ej)))
    print('#{} {}'.format(test_case,dfs_ans(si,sj)))