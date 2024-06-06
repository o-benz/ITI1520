#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

n=int(input("SVP Entrer un entier n = "))
p=int(input("SVP Entrer un 2eme entier p =  "))

print("Les valeurs de n inférieurs à p sont :")

for p in range(n, p):
    print(p)
    p-1

p=p+1
q=p%2

print("2eme boucle")
print("Les valeurs de p impairs sont :")


if (q==1):
    while(p>0):
        print(p)
        p=p-2
else :
    p=p-1
    while(p>0):
        print(p)
        p=p-2
