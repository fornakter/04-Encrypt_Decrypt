a = input("Podaj slowo:")
tab = []
for i in range(len(a)):
    tab.append(ord(a[i]))
print(tab)
i = 0
for i in range (len(tab)):
    tab[i] = tab[i]-22
print(tab)
print(a)
for i in range(len(tab)):
    tab[i] = tab[i]+22
print(tab)
for i in range(len(tab)):
    a = tab[i]
    print(chr(a), end='')
print()
