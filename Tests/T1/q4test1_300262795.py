#Omar Benzekri 300262795

def helper(s1,s2):
     if int(s1)%2==0 and int(s2)%2==0:
          return int(s1)+int(s2)
     elif int(s1)%2==1 and int(s2)%2==1:
          return int(s1)+int(s2)
     elif int(s1)%2==0 and int(s2)%2==1:
          return int(s1)*int(s2)
     elif int(s1)%2==1 and int(s2)%2==0:
          return int(s1)*int(s2)

def yangtze(s):
     s=list(s)
     c1=0
     c2=1
     s1=""
     s2=""
     while c1<len(s):
          s1+=s[c1]
          c1+=3
     while c2<len(s):
          s2+=s[c2]
          c2+=1
          s2+=s[c2]
          c2+=2
     print ("La chaine composée de blocs de taille 1 est :",s1)
     print ("La chaine composée de blocs de taille 2 est:",s2)
     print ("Le résultat est donc: ",helper(s1,s2))

     
 
