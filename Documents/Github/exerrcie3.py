def puissance2k(x,k):
    while k > 0 :
        x *= x
        k -= 1
    return x
def fact(n):
    
    if n<2:
        return 1
    else:
        return n*fact(n-1)
num = int(input("saisie un nombre\n"))
p = int(input("saisie une puissnce\n"))
f = int(input("saisie le factorielle\n"))

r = puissance2k(num,p)
n = fact(f)
somme = int(r)/int(n)
print(str(somme))
