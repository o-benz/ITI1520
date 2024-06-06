#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def move_zeros_no_extra(x):
    f=0
    nzero=0
    while f<len(x)and f+nzero<len(x):
        if x[f]==0:
            nzero+=1
            for i in range(f,len(x)-1):
                x[i]=x[i+1]
            x[-1]=0
        else:
            f+=1

l=[1,3,5,0,7]
print(l)
move_zeros_no_extra(l)
print(l)
