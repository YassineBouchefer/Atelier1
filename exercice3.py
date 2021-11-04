def somme(n):
    if(n==0):
        return 0
    else:
        return n+somme(n-1)
k=int(input("donner un nombre : "))
print("la somme de 1 à %d est : %d",k,sommme(k))