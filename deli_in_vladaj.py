##########################################################################
# Želimo definirati pivotiranje na mestu za tabelo a.
# Ker bi želeli pivotirati zgolj dele tabele a, se hkrati omejimo na
# del tabele, ki se nahaja med indeksoma start in end.
# Na primer, za start = 0 in end = 8 tabelo
#
# [10, 4, 5, 15, 11, 2, 17, 0, 18]
#
# preuredimo v
#
# [0, 2, 5, 4, 10, 11, 17, 15, 18]
#
# (Možnih je več različnih rešitev, pomembno je, da je element 10 pivot.)
#
# Sestavi funkcijo pivot_list(a, start, end), ki preuredi tabelo a tako,
# da bo a[start] postal pivot za del tabele med indeksoma start in end.
# Funkcija naj vrne indeks, na katerem je po preurejanju pristal pivot.
# Funkcija naj deluje v času O(n), kjer je n dolžina tabele a.
# Primer:
#
#     >>> a = [10, 4, 5, 15, 11, 2, 17, 0, 18]
#     >>> pivot_list(a, 1, 7)
#     3
#     >>> a
#     [10, 2, 0, 4, 11, 15, 17, 5, 18]
##########################################################################
def pivot_list1(a, start, end):
    pivot = a[start]
    spodnji_ind = start
    zgornji_ind = end
    while spodnji_ind  < zgornji_ind :
        if a[spodnji_ind]>pivot:
            if a[zgornji_ind] < pivot:
                a[spodnji_ind], a[zgornji_ind] = a[zgornji_ind], a[spodnji_ind]
            zgornji_ind -= 1
        spodnji_ind += 1
    a[start] = a[spodnji_ind]
    a[spodnji_ind] = pivot
        
    return a
def pivot_list(a, start, end):
    pivot = a[start]
    spodnji_ind = start
    zgornji_ind = end
    while spodnji_ind  != zgornji_ind :
        if zgornji_ind > len(a)-1:
            print(a)
        if a[spodnji_ind+1] <= pivot:
            spodnji_ind += 1
        elif a[zgornji_ind] > pivot:
            zgornji_ind -= 1
        else:
            temp = a[spodnji_ind +1]
            a[spodnji_ind+1] = a[zgornji_ind]
            a[zgornji_ind] = temp
    a[start] = a[spodnji_ind]
    a[spodnji_ind] = pivot
    return spodnji_ind, a
           
##########################################################################
# Tabelo a želimo urediti z algoritmom hitrega urejanja, ki smo ga
# spoznali na predavanjih.
#
# Napišite funkcijo quicksort(a), ki uredi tabelo a s pomočjo pivotiranja.
# Poskrbi, da algoritem deluje 'na mestu', torej ne uporablja novih tabel.
#
# Namig: definirajte pomožno funkcijo quicksort_part(a, start, end), ki
#        uredi zgolj del tabele a.
#
#   >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
#   >>> quicksort(a)
#   [2, 3, 4, 5, 10, 11, 15, 17, 18]
##########################################################################
def quicksort_part(a, start, end):
    if start == end:
        return 
    ind_pivot,a = pivot_list(a, start, end)
    
    if start < end:  
        quicksort_part(a, start, ind_pivot-1)
        quicksort_part(a, ind_pivot+1, end)
    

##########################################################################
# V tabeli a želimo poiskati vrednost k-tega elementa po velikosti.
# Na primer, če je
#
# >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
#
# potem je tretji element po velikosti enak 5, ker so od njega manši
# elementi 2, 3 in 4. Pri tem štejemo indekse od 0 naprej, se pravi
# "ničti" element je 2.
#
# Sestavite funkcijo kth_element(a, k), ki v tabeli a poišče k-ti element
# po velikosti. Funkcija sme spremeniti tabelo a.
#
# Namig: ponovno si pomagaj s pomožno funkcijo.
##########################################################################
