import sys

n=[]
t = int(input().strip())
for a0 in range(0,t):
    n.append(int(input().strip()))
for i in range(t):
    list_=[]
    for j in range(n[i]):
        if(j%3==0 or j%5==0):
            list_.append(j)
    sum_=sum(list_)
    print(sum_)    
        