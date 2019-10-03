#Partial Solution
#Link to the problem :- https://www.codechef.com/MAY19B/problems/REDONE
for _ in range(int(input())):
    N = int(input())
    L = [1]
    if N == 1:
        print(1)
    else:
        for i in range(1, N):
            L.append((L[-1]*(i+2)) + (i+1))
        print(L[-1]%1000000007)
