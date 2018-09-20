from itertools import product

A=input().split()
A=list(map(int,A))
B=input().split()
B=list(map(int,B))

for x in product (A,B):
    print (x, end=' ')
