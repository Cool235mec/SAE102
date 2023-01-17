def triFusion(L):
    if len(L) <= 1:
        return L
    else:
        return fusion(triFusion(L[:len(L)//2]),triFusion(L[len(L)//2:]))
    
def fusion(A,B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] <= B[0]:
        return [A[0]] + fusion( A[1:] , B )
    else:
        return [B[0]] + fusion( A , B[1:] )
    

#def tri_insertion(tableau, gap, debut):
#    for i in range(gap + debut,len(tableau),gap):
#        en_cours = tableau[i]
#        j = i
#        #décalage des éléments du tableau }
#        while j>0 and tableau[j-gap]>en_cours:
#            tableau[j]=tableau[j-gap]
#            j = j-gap
#         #on insère l'élément à sa place
#        tableau[j]=en_cours
#    return(tableau)
#
#def tri_shell (tableau):
#    for gap in [i for i in range(len(tableau)/2,1,i/2)]:
#        # Pour chaque sous-tableau ...
#           for debut in range(0,gap):
#            #... on fait un tri par insertion
#                tableau = tri_insertion(tableau,gap,debut)
#    return(tableau)

