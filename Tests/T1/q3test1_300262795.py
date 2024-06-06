#Omar Benzekri 300262795

def helper(s1,s2):
     if int(s1)%2==0 and int(s2)%2==0:
          print(int(s1)+int(s2))
     if int(s1)%2==1 and int(s2)%2==1:
          print(int(s1)+int(s2))
     if int(s1)%2==0 and int(s2)%2==1:
          print(int(s1)*int(s2))
     if int(s1)%2==1 and int(s2)%2==0:
          print(int(s1)*int(s2))
