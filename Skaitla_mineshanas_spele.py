# Skaitļa minēšanas spēle
# Izveidoja: Jaroslavs Frolovs

from random import randint
print('Datorspēle \'Uzmini skaitli\'.')
print('Dators "iedomājas" veselo skaitli no 1 līdz 10. ', end='\n\n')
print('Uzminiet skaitli. ')
Datora_skaitlis = randint(1,10)

neuzmineja = True
while neuzmineja: #kamēr neuzminēja, cikls ar pirmspārbaudi
    ievade = input('Ievadiet skaitli no 1 līdz 10, ieskaitot 10: ')
    Cilveka_skaitlis = int(ievade)
    if Datora_skaitlis < Cilveka_skaitlis:
        print('Neuzminējāt. Ievadiet mazāku skaitli. ')
    else:
        if Datora_skaitlis > Cilveka_skaitlis:
            print('Neuzminējāt. Ievadiet lielāku skaitli. ')
        else:
            neuzmineja = False

print('Uzminējāt!!!')
