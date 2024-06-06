def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   i = 0
   while i < len(tab):
      j = 0
      while j < len(tab[0]):
         tab[i][j] = '-'
         j += 1
      i += 1
      
      
    # a completer
    
    # retourne rien

      
def verifieGagner(tab):  
   '''(list) ->  bool
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   * Verifie s'il y a un gagnant.
   * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
   * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
   * ou "Joueur O a gagné!") et retourne True.
   * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
   * affiche "Match nul" et retourne True.
   * Si le jeu n'est pas fini, retourne False.
   * La fonction appelle les fonctions testLignes, testCols, testDiags
   * pour verifier s'il y a un gagnant.
   * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
   '''
   x = testLignes(tab)
   y = testCols(tab)
   z = testDiags(tab)
   m = testMatchNul(tab)
   # Lignes
   if x != '-':
      print('Joueur ', x, ' a gagné!')
      return True
   # Colonnes
   if y != '-':
      print('Joueur ', y, ' a gagné!')
      return True
   # Diagonales
   if z != '-':
      print('Joueur ', z, ' a gagné!')
      return True
   # Match nul
   if m:
      print('Match nul')
      return True
   return False


 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   i = 0
   while i < len(tab):
      j = 0
      x = tab[i][0]
      if x == '-':
         i += 1
      else:
         win = True
         while j < len(tab[0]):
            if tab[i][j] != x:
               i += 1
               win = False
               break
            else:
               j += 1
         if win:
            return x  
   return '-' # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   j = 0
   while j < len(tab):
      i = 0
      x = tab[0][j]
      if x == '-':
         j += 1
      else:
         win = True
         while i < len(tab[0]):
            if tab[i][j] != x:
               j += 1
               win = False
               break
            else:
               i += 1
         if win:
            return x   
   return '-'   #a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   # premiere diagonale
   i = 0
   x = tab[0][0]
   if x != '-':
      win = True
      while i < len(tab):
         if tab[i][i] == x:
            i += 1
         else:
            win = False
            break
      if win:
         return x
   # 2e diagonale
   y = tab[0][len(tab)-1]
   if y != '-':
      win = True
      i = 0
      while i < len(tab):
         if tab[i][len(tab)-i-1] == y:
            i += 1
         else:
            win = False
            break
      if win:
         return y
   return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   i = 0
   while i < len(tab):
      j = 0
      while j < len(tab[0]):
         if tab[i][j] == '-':
            return False
         j += 1
      i += 1
   return True

