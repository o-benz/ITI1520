#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def move_zeros_with_return(x):
    tmp=[0]*len(x)
    i=0
    for xi in x:
        if xi != 0:
            tmp[i]=xi
            i+=1
    for i in range (len(x)):
        x[i]=tmp[i]
l=[1,0,3,0,0,5,7]
print(l)
move_zeros_with_return(l)
print(l)
