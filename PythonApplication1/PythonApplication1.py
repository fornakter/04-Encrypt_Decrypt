tab = []

a = input("Podaj slowo:")

for i in range(len(a)):
    tab.append(ord(a[i]))

i = 0
for i in range(len(tab)):
    tab[i] = tab[i]-22
print("Zakodowane:", tab)

print("Odkodowane")
for i in range(len(tab)):
    tab[i] = tab[i]+22
    a = tab[i]
    print(chr(a), end='')
