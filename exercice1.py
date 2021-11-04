# x!/x = (x-1)! for any x>0
i=1
somme=0
def facto(x):
    if(x==0,1):
        return 1
    else:
        return x*facto(x-1)

while(i<k): # I did i<k because i want to stop after adding k-1
    somme+=facto(i)
    i+=1
k=int (input("give a number : "))
print(" la somme est : %d ",somme)