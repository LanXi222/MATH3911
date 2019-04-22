print('One emperor, two aristocrats, three officials and an even number of commons divide 100 gold coins. The emperor will propose a plan to divide the gold coins. If the plan is not passed, the emperor will be overthrown. It then follows that the second most powerful character(an aristocrat) will propose a new plan, and she will also be overthrown if the plan is not passed. So on and so forth.\n The kingdom has a weighted voting system, and the weight grows larger as the character is on a higher hierachy. The plan will be passed if the sum of weights of supporters is at least half of the sum of weights.\n')
z = int(input('Enter the weight of officials (the weight of commons is 1): '))
y = int(input('Enter the weight of aristocrats: '))
x = int(input('Enter the weight of Emperor: '))
n = int(input('Enter the number of commons (an even number) : '))

from math import *
dist=[0]*7
dist[0]=[0]*n
for i in range(n):
    if i==0:
        dist[0][i]=1
    elif i==n-1:
        dist[0][i]=100-n/2
    elif i%2==0:
        dist[0][i]=0
    else:
        dist[0][i]=1
print(dist[0])

dist[1]=[0]*(n+1)
count=0
for i in range(n+1):
        if count<min(dist[0].count(0),ceil(0.5*(z+n)-z)):
            if dist[0][i]==0:
                dist[1][i]=1
                count+=1
            else:
                dist[1][i]=0
        else:
            dist[1][i]=0
        if i==n:
            dist[1][i]=floor(min(100, 100-(0.5*(z+n)-z)))
for i in range(n+1):
    if count>=dist[0].count(0) and count<ceil(0.5*(z+n)-z) and dist[0][i]==1:
        dist[1][i]=2
        count+=1
print(dist[1])

                             

dist[2]=[0]*(n+2)
count=0
for i in range(n+2):
    if dist[1].count(0)>=ceil((0.5*(2*z+n)-z)):
        if count<ceil(0.5*(2*z+n)-z):
            if dist[1][i]==0:
                dist[2][i]=1
                count+=1
            else:
                dist[2][i]=0
        else:
            dist[2][i]=0
        if i==n+1:
            dist[2][i]=floor(min(100, 100-(0.5*(2*z+n)-z)))
print(dist[2])

dist[3]=[0]*(n+3)
count=0
for i in range(n+3):
    if dist[2].count(0)>=ceil(0.5*(3*z+n)-2*z+1):
        dist[3][-3]=1
        if count<ceil(0.5*(3*z+n)-2*z):
            if dist[2][i]==0:
                dist[3][i]=1
                count+=1
            else:
                dist[3][i]=0
        elif i!=n:
            dist[3][i]=0
        if i==n+2:
            dist[3][i]=floor(min(100, 100-(0.5*(3*z+n)-2*z+1)))
print(dist[3])

dist[4]=[0]*(n+4)
count=0
for i in range(n+4):
    if dist[3].count(0)>=ceil(0.5*(y+3*z+n)-2*z-y+2) and z>=2:
        dist[4][-3]=1
        dist[4][-4]=2
        if count<ceil(0.5*(y+3*z+n)-2*z-y) and (i<n):
            if dist[3][i]==0:
                dist[4][i]=1
                count+=1
            else:
                dist[4][i]=0
        elif i!=n and i!=n+1:
            dist[4][i]=0
        if i==n+3:
            dist[4][i]=floor(min(100, 100-(0.5*(y+3*z+n)-2*z-y+3)))
    if z<2:
        dist[4][-3]=1
        if count< ceil(0.5*(y+3*z+n)-z-y) and i<n:
            if dist[3][i]==0:
                dist[4][i]=1
                count+=1
            else:
                dist[4][i]=0
        elif i!=n+1:
            dist[4][i]=0
        if i==n+3:
            dist[4][i]=floor(min(100, 100-(0.5*(y+3*z+n)-z-y+1)))
print(dist[4])

dist[5]=[0]*(n+5)
count=0
for i in range(n+5):
    if dist[4].count(0)>=ceil(0.5*(2*y+3*z+n)-3*z-y+3) and z>2:
        dist[5][-3]=1
        dist[5][-4]=2
        dist[5][-5]=3
        if count<ceil(0.5*(2*y+3*z+n)-3*z-y) and (i<n):
            if dist[4][i]==0:
                dist[5][i]=1
                count+=1
            else:
                dist[5][i]=0
        elif i!=n and i!=n+1 and i!=n+2:
            dist[5][i]=0
        if i==n+4:
            dist[5][i]=floor(min(100, 100-(0.5*(2*y+3*z+n)-3*z-y+6)))
    if z<2:
        dist[5][-3]=1
        dist[5][-5]=1
        if count< ceil(0.5*(2*y+3*z+n)-2*z-y) and i<n:
            if dist[4][i]==0:
                dist[5][i]=1
                count+=1
            else:
                dist[5][i]=0
        elif i!=n+2 and i!=n:
            dist[5][i]=0
        if i==n+4:
            dist[5][i]=floor(min(100, 100-(0.5*(y+3*z+n)-2*z-y+2)))
    if z==2:
        dist[5][-3]=1
        dist[5][-4]=2
        if count< ceil(0.5*(2*y+3*z+n)-2*z-y) and i<n:
            if dist[4][i]==0:
                dist[5][i]=1
                count+=1
            else:
                dist[5][i]=0
        elif i!=n+2 and i!=n+1:
            dist[5][i]=0
        if i==n+4:
            dist[5][i]=floor(min(100, 100-(0.5*(y+3*z+n)-2*z-y+3)))
print(dist[5])


dist[6]=[0]*(n+6)
count=0
for i in range(n+6):
    if dist[5].count(0)>=ceil(0.5*(x+2*y+3*z+n)-3*z-y-x+4) and z>3:
        dist[6][-3]=1
        dist[6][-4]=2
        dist[6][-5]=3
        dist[6][-6]=4
        if count<ceil(0.5*(x+2*y+3*z+n)-3*z-y-x) and (i<n):
            if dist[5][i]==0:
                dist[6][i]=1
                count+=1
            else:
                dist[6][i]=0
        elif i!=n and i!=n+1 and i!=n+2 and i!=n+3:
            dist[6][i]=0
        if i==n+5:
            dist[6][i]=floor(min(100, 100-(0.5*(x+2*y+3*z+n)-3*z-y-x+10)))
    if z==3:
        dist[6][-3]=1
        dist[6][-4]=2
        dist[6][-5]=3
        if count< ceil(0.5*(x+2*y+3*z+n)-2*z-y-x) and i<n:
            if dist[5][i]==0:
                dist[6][i]=1
                count+=1
            else:
                dist[6][i]=0
        elif i!=n+1 and i!=n+2 and i!=n+3:
            dist[6][i]=0
        if i==n+5:
            dist[6][i]=floor(min(100, 100-(0.5*(y+3*z+n)-2*z-y-x+6)))
    if z==2:
        dist[6][-3]=1
        dist[6][-4]=2
        dist[6][-6]=1
        if count< ceil(0.5*(x+2*y+3*z+n)-2*z-y-x) and i<n:
            if dist[5][i]==0:
                dist[6][i]=1
                count+=1
            else:
                dist[6][i]=0
        elif i!=n and i!=n+2 and i!=n+3:
            dist[6][i]=0
        if i==n+5:
            dist[6][i]=floor(min(100, 100-(0.5*(x+2*y+3*z+n)-2*z-y-x+4)))
    if z==1:
        dist[6][-3]=1
        dist[6][-5]=1
        if count< ceil(0.5*(x+2*y+3*z+n)-z-y-x) and i<n:
            if dist[5][i]==0:
                dist[6][i]=1
                count+=1
            else:
                dist[6][i]=0
        elif i!=n+1 and i!=n+3:
            dist[6][i]=0
        if i==n+5:
            dist[6][i]=floor(min(100, 100-(0.5*(x+2*y+3*z+n)-z-y-x+2)))
print(dist[6])
