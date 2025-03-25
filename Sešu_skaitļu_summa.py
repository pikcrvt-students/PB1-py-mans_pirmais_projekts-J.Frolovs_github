'''Sešu skaitļu summa.
   Izveidoja: Jaroslavs Frolovs
'''
print('Sešu skaitļu summas aprēķināšana.')
print()   # pariet nākamajā rindā.

summa = 0
for x in range(6):   # skaitītājs no 0 līdz 6 (neieskaitot)
    skaitlis = int(input('Ievadiet ' + str(x + 1) + '. Veselo skaitļi: ') )
    summa = summa + skaitlis # summa apreķināšana

print('\nSumma ir', summa) # rezultāta izvade
