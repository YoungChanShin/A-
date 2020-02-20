import sys
sys.stdin=open('input.txt')

def Calculate(a,c,b):
    if c == '+':
        return int(a)+int(b)
    elif c == '-':
        return int(a)-int(b)
    elif c == '*':
        return int(a)*int(b)
# N = int(input())
# A = list(input())
def find_max_val(N,A):
    if N == 1:
        result = A[0]
    elif N < 9:
        S1 = int(A[0])
        S2 = Calculate(A[0], A[1], A[2])
        for i in range(2, len(A) - 1, 2):
            temp = S1
            S1 = S2
            S2 = max(Calculate(S2, A[i + 1], A[i + 2]), Calculate(temp, A[i - 1], Calculate(A[i], A[i + 1], A[i + 2])))
        result = S2
    else:
        S1 = int(A[0])
        S2 = Calculate(A[0], A[1], A[2])
        i = 2
        S3 = max(Calculate(S2,A[i+1],A[i+2]), Calculate(S1,A[i-1],Calculate(A[i],A[i+1],A[i+2])))
        i = 4
        S4 = max(Calculate(S3, A[i + 1], A[i + 2]), Calculate(S2, A[i - 1], Calculate(A[i], A[i + 1], A[i + 2])))
        for i in range(6, len(A) - 1, 2):
            minus = -(2**31)
            if Calculate(A[i], A[i + 1], A[i + 2]) < 0 and A[i - 1] == '*' and Calculate(A[i - 4], A[i - 3], A[i - 2]) < 0:
                minus = Calculate(S1,A[i-5],Calculate(A[i], A[i + 1], A[i + 2]))*Calculate(A[i - 4], A[i - 3], A[i - 2])
            S1 = S2
            S2 = S3
            S3 = S4
            S4 = max(Calculate(S4, A[i + 1], A[i + 2]), Calculate(S2, A[i - 1], Calculate(A[i], A[i + 1], A[i + 2])))
            S4 = max(minus, S4)
        result = S4
    print(result)

ts=int(input())
for test_case in range(ts):
    N=int(input())
    A=input()
    find_max_val(N,A)