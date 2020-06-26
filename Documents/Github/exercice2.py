print("saisie une serie de nombre\n")
tab = []

while True:
    num = input("saisie un nombre\n")
    if(int(num) == 0):
        break
    else:
        tab.append(int(num)) 



somme = sum(tab)
pos_count, neg_count = 0, 0
for num in tab: 
      
    if num >= 0: 
        pos_count += 1
  
    else: 
        neg_count += 1
print(".........................resultat.....................")

print("nombre positive: ", pos_count) 
print("nombre ngative: ", neg_count)
print("la somme est "+str(somme)+"\n")

