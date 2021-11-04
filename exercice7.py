def renverse(string): 
    if len(string) == 0: 
        return string 
    else: 
        return renverse(string[1:]) + string[0] 
  
string = "Tester"
  
print ("la chaine de caractère originale est : ",end="") 
print (string) 
  
print ("la chaine de caractère renversée est : ",end="") 
print (renverse(string))  