test_matrix = [[1 , 2 , 0 ],
               [ 2 , 4 , 5 ],
               [ 7 , 0 , 1 ]]

from functools import lru_cache
memoiziraj = lru_cache(maxsize=None)


def najdaljse_skupno(xs, ys):
    if not xs or not ys:
        return ()
    elif xs[0] == ys[0]:
        return (xs[0],) + najdaljse_skupno(xs[1:], ys[1:])
    else:
        l = najdaljse_skupno(xs, ys[1:])
        d = najdaljse_skupno(xs[1:], ys)
        return l if len(l) >= len(d) else d


@memoiziraj
def najdaljsi_podpalindrom(niz):
    if len(niz) <= 1:
        return niz
    elif niz[0] == niz[-1]:
        return niz[0] +  najdaljsi_podpalindrom(niz[1:-1]) + niz[-1]
    else:
        levi = najdaljsi_podpalindrom(niz[:-1])
        desni = najdaljsi_podpalindrom(niz[1:])
        return levi if len(levi) >= len(desni) else desni
##########################################################################################
def max_cheese(m):
    @memoiziraj
    def max_pomozna(vrstica, stolpec):
        if vrstica==stolpec==0:
            return m[0][0]
        elif vrstica==0:
            return m[vrstica][stolpec] + max_pomozna(vrstica, stolpec-1)
        elif stolpec == 0:
            return m[vrstica][stolpec] + max_pomozna(vrstica-1, stolpec )
        else:
            return m[vrstica][stolpec] + max (max_pomozna(vrstica, stolpec-1),
                                              max_pomozna(vrstica-1, stolpec )
                                              )

    return max_pomozna(len(m)-1, len(m[0])-1)

######################################################################
#Rešujemo problem stolpov, ko smo ga spoznali na predavanjih.
#   Imamo štiri različne tipe gradnikov, dva modra in dva rdeča.
#   Modri gradniki so višin 2 in 3, rdeči pa višin 1 in 2.

#   Napiši funkcijo "alternating_towers height", ki za podano višino "height"
#   izpiše število različnih stolpov podane višine, kjer se barva gradnikov
#   izmenjuje (rdeč na modrem, moder na rdečem itd.).

#   Namig: Uporabi dve pomožni funkciji. Za medsebojno rekurzijo uporabi
#          ukaz "and".
#   ----------
#   # alternating_towers 10;;
#   - : int = 35
#############################################################################
    
def stolpi(n):
    if n == 0:
        return 1
    else:
        return modri_stolpi(n) + rdeci_stolpi(n)

def modri_stolpi(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    vsota = 0
    for k in [2,3]:
        vsota += rdeci_stolpi(n - k)
    return vsota

def rdeci_stolpi(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    vsota = 0
    for k in [1,2]:
        vsota += modri_stolpi(n - k)
    return vsota
