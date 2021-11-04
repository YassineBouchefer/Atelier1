mtrrows = int(input('le nombre de lignes = '))
mtrcols = int(input('le nombre de colones = '))
mtr = []
for n in range(mtrrows):
    l = list(map(int, input(
        'Entrer {'+str(mtrcols)+'} l elements de ligne {'+str(n+1)+'} séparé par espace = ').split()))
    mtr.append(l)
gvnele = int(input('entrer un element = '))
tempo = 0
for n in range(mtrrows):
    for m in range(mtrcols):
        if(mtr[n][m] == gvnele):
            print('l element donné {', gvnele, '} est présent dans la ligne {' +
                  str(n+1)+'} et colonne {'+str(m+1)+'}')
            tempo = 1
if(tempo == 0):
    print('l element donné n existe pas dans la matrice.')