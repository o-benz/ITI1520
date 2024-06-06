#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

def read_raw(file):
    '''str->list of str
    Renvoie une liste de chaînes qui ont été stockées dans un fichier.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str
    La fonction prend en entrée une liste de caractères.
    Elle renvoie une nouvelle liste contenant les mêmes caractères que l
    sauf que un de chaque caractère apparaissant un nombre impair de fois
    dans l est supprimé et tous les caractères * sont supprimés 

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''
    clean_board=[]

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    for i in l:
        count = l.count(i)
        if i not in clean_board and i != '*':
            if count % 2 == 0:
                for x in range(count):
                    clean_board.append(i)
            else:
                count = count-1
                for x in range(count):
                    clean_board.append(i)
    return clean_board
    


def  is_rigorous(l):
    '''list of str->bool
    Renvoie True si chaque caractère de la liste apparaît exactement 2 fois ou si la liste est vide.
    Sinon, elle renvoie False. 
    
    Précondition: vous pouvez supposer que chaque élément de la liste apparaît un nombre pair de fois
    (c'est-à-dire que la liste est nettoyée par la fonction clean_up)
    >>>  is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>>  is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    for i in l:
        count = l.count(i)
        if count != 2:
            return False
    return True
        

    
#programme principal
file=input("Entrer le nom du fichier: ")
file=file.strip()
b=read_raw(file)
print("\nAvant clean-up:\n", b)
b=clean_up(b)
print("\nAprès clean-up:\n", b)
if is_rigorous(b):
    print("\nCette liste est maintenant rigoureuse; elle n’a aucun * et elle a "+str(len(b))+" caractères.")
else:
    print("\nCette liste n’a aucun * mais n'est pas rigoureuse et a "+str(len(b))+" caractères.")
     
