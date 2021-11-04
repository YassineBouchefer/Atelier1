
    i=0
    j=1
def fibo(x):
    n=i+j
    i=j
    j=n
    while (n==1):
        print("0")
        print("1")
    if (x-2==0):
        return print(n)
    else:
        print(n)
        return fibo(x-1)
k=int(input("give a number : "))
print(fibo(k))