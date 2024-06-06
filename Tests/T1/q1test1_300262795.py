# Omar Benzekri 300262795

def irtysh(n):
     c=0
     if n==1:
          x=int(input("Entrer un entier positif: "))
          y=x
          while y>0:
               if x%y==0:
                    c+=1
               y-=1
          if c!=3:
               return False
          if c==3:
               return True
     if n!=1:
          while n>9999:
               n-=10000
          while n>999:
               n-=1000
          n/=100
          return int(n)
