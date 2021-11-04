# tri à bull
def bulle(tab):
    n = len(tab)
    for i in range(n):    # Traverser tous les éléments du tableau
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1] :    # échanger si l'élément trouvé est plus grand que le suivant
                tab[j], tab[j+1] = tab[j+1], tab[j]
tab = [9, 2, 5, 3, 2, 4, 6, 7]   
 
bulle(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])
# tri par selection
# c'est l'inverse du tri à bull
def selection(tab):
   for i in range(len(tab)):
       min = i    # Trouver le min
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
# Programme pour tester le code ci-dessus
tab = [9, 2, 5, 3, 2, 4, 6, 7]  
 
selection(tab)
 
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])
# tri par insertion
def insertion(tab): 
    for i in range(1, len(tab)):   # Parcour de 1 à la taille du tab
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
# Programme pour tester le code ci-dessus
tab = [9, 2, 5, 3, 2, 4, 6, 7]  
insertion(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % tab[i])