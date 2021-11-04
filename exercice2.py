i=1
bin=0
def convert(x):
    if(x==1):     #
        return 1  # 'k=0' et 'k=1' sont des cas particuliers qu'on peut pas ajouter dans la boucle donc j'ai donné le résultat directement.
    elif(x==0):   #
        return 0  #
    else:         
        while(x>1): # on va toujours diviser 'x' par '2' jusqu'à ce qu'elle arrive à '1' ou '0'.
            if(x%2==0):  #
                i*=10    # si 'x%2=0' donc le chiffre qu'on va écrire est '0'.
                x/=2     #
            else:        
                bin+=i #
                i*=10  # si 'x%2=1' donc le chiffre qu'on va écrire est '1'.
                x/=2   #
        return bin
k=int (input("give a number"))
print("the binary number of %d is : %d ",k,convert(k))