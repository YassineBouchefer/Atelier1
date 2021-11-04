i=0
def chif(n):
    if (n==0):
        return i
    i+=1
    else:
        return chif(n/10)
k=int(input("give a number : "))
print("le nombre de chiffre est", chif(k))