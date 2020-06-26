taille=input("********saisie 5 nombre je te donne le plus grand et le plus peitit\n")
tab = []
for i in range(int(taille)):
    num = input("saisie le "+str(i+1)+" Nombre\n")
    tab.append(num)

print(".........................resultat.....................")
print("le minimum est"+min(tab) +"\n")
print("le minimum est"+max(tab) +"\n")
