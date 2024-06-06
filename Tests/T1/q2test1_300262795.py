#Omar Benzekri 300262795

def danube(s):
     s=list(s)
     A=s.count("A")
     B=s.count("B")
     C=s.count("C")
     F=s.count("F")
     moya=round((A/len(s))*100,2)
     moyb=round((B/len(s))*100,2)
     moyc=round((C/len(s))*100,2)
     moyf=round((F/len(s))*100,2)
     print(moya,"% des étudiants ont A")
     print(moyb,"% des étudiants ont B")
     print(moyc,"% des étudiants ont C")
     print(moyf,"% des étudiants ont F")
     moy=" "
     if moya>=moyb and moya>=moyc and moya>=moyf:
          print("La moyenne est A")
     elif moyb>=moya and moyb>=moyc and moyb>=moyf:
          print("La moyenne est B")
     elif moyc>=moyb and moyc>=moya and moyc>=moyf:
          print("La moyenne est C")
     elif moyf>=moyb and moyf>=moyc and moyf>=moya:
          print("La moyenne est F")

     
           


          
 
