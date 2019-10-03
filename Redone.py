#All Correct
#Link to the problem :- https://www.codechef.com/MAY19B/problems/REDONE


res=[0]*10000001
def fact(n):
    if res[n]!=0:
        return res[n]%mod
    elif n>=0:
        res[0]=1
        for i in range(1,n+1):
            res[i]=(i*res[i-1])%mod
        return res[n]%mod

for i in range(T):
    N=int(input())
    print(fact(N+1)-1)


""" #Another approach but is inefficient if we consider space complexity.
mod=1000000007
L = [1]
for i in range(1, 1000000):
    L.append(((L[-1]*(i+2)) + (i+1))%(mod))
    
T = int(input())
for i in range(T):
    N = int(input())
    print(L[N-1])
"""
