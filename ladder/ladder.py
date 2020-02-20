import sys
sys.stdin=open('input.txt')

def go(start):
    while start<N*H:
        # print(start)
        if start%N==0:
            if (start//N)*(N-1) in ladder:
                start+=N+1
            else:
                start+=N
            continue
        if start%N==N-1:
            if ((start//N)+1)*(N-1)-1 in ladder:
                start+=N-1
            else:
                start+=N
            continue
        if (start//N)*(N-1)+(start%N) in ladder:
            start+=N+1
            continue
        if (start//N)*(N-1)+(start%N)-1 in ladder:
            start+=N-1
            continue
        else:
            start+=N
    return start%N

def check(N,H,ladder):
    flag=0
    for i in range(N):
        ret=go(i)
        # print(ret)
        if ret%(N*H) != i:
            break
        if i==N-1:
            flag=1
    return flag

def add_if_possible(N,H,ladder,NL):
    if j not in ladder:
        if (j+1)%(N-1)==1:
            if (j+1) not in ladder:
                temp.append(j)
                flag=check(N,H,temp)

        if flag:
            if (j-1)%(N-1)==N-1:
                if (j-1) not in ladder:
                    temp.append(j)
                    flag=check(N,H,temp)
                    
        if flag:
            if ((j+1) not in ladder) and ((j-1) not in ladder):
                temp.append(j)
                flag=check(N,H,temp)
    return ladder

def add_lad(lad,N):
    '''
    lad를 ladder에 추가할 수 있다면 더하고 추가했는지 참 거짓 여부를 반환 
    '''
    if lad in ladder:
        return False
    if lad%(N-1)==0:
        if lad+1 in ladder:
            return False
        ladder.append(lad)
        return True
    if lad%(N-1)==N-1:
        if lad-1 in ladder:
            return False
        ladder.append(lad)
        return True
    if lad-1 in ladder or lad+1 in ladder:
        return False
    ladder.append(lad)
    return True
def remove_ladder(lad):
    ladder.remove(lad)

T = 7
for test_case in range(1,1+T):
    # print('====',test_case)
    N,M,H=map(int,input().split())
    ladder=[]
    cnt=0
    flag=False
    for i in range(M):
        a,b=map(int,input().split())
        ladder.append((a-1)*(N-1)+b-1)
    #사다리 추가 안 했을 때
    if check(N,H,ladder):
        print(test_case,cnt)
        continue
    cnt=1
    #사다리 1개 추가
    for lad in range((N-1)*H):
        if add_lad(lad,N):
            if check(N,H,ladder):
                print(test_case,cnt)
                flag=True
                continue
            remove_ladder(lad)
    cnt=2
    #사다리 두개 추가
    if not flag:
        for lad1 in range((N-1)*H-1):
            if add_lad(lad1,N):
                for lad2 in range(lad1, (N-1)*H):
                    if add_lad(lad2,N):
                        if check(N,H,ladder):
                            print(test_case,cnt)
                            flag=True
                            continue
                        remove_ladder(lad2)
                remove_ladder(lad1)
    # 사다리 세개 추가
    cnt=3
    if not flag:
        for lad1 in range((N-1)*H-2):
            if add_lad(lad1,N):
                for lad2 in range(lad1+1, (N-1)*H-1):
                    if add_lad(lad2,N):
                        for lad3 in range(lad2+1,(N-1)*H):
                            if add_lad(lad3,N):
                                if check(N,H,ladder):
                                    print(test_case,cnt)
                                    flag=True
                                    continue
                                remove_ladder(lad3)
                        remove_ladder(lad2)
                remove_ladder(lad1)
    if not flag:
        cnt=-1
        print(test_case,cnt)