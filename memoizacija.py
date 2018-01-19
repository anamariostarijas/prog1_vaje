from functools import lru_cache

# Cilj: izračunajte vrednosti Fibonaccijevega zaporadja za 100, 500, 1000,
# 10**5, and 10**6 člen.
# Za vsako definicijo preizkusite kako pozne člene lahko izračuante in poglejte
# zakaj se pojavi problem (neučinkovitost, pregloboka rekurzija,
# premalo spomina ...).

# Definirajte naivno rekurzivno različico.
# Omejitev: Prepočasno.
def fib(n):
    if n==0 | n ==1:
        return n
    else:
        return fib(n-2) + fib(n-1)
        
# Z uporabo dekoratorja izboljšajte naivno različico.
# Omejitev: Preseže največjo dovoljeno globino rekurzija za ~350.
#tako si sproti zapomni rezutate, če rezultata še ni, dela rekurzivno
@lru_cache()
def fib_cache(n):
   if n <= 1:
       return n
   else:
       return fib_cache(n-1) + fib_cache(n-2)
# Nariši drevo klicov za navadno rekurzivno fib funkcijo pri n=5 in
# ugotovi kateri podproblemi so klicani večkrat.

# Definirajte rekurzivno memoizirano funkcijo fib brez uporabe dekoratorja.
# Omejitev: Preseže največjo dovoljeno globino rekurzija za ~1000.
def fib_memo_rec(n):
    rez = [None] * max(n+1, 2)
    rez[0]=0
    rez[1] = 1
    def aux(n):
        if rez[n] != None:
            return rez[n]
        else:
            x= aux(n-1) + aux(n-2)
            rez[n] = x
            return x
    return aux(n)
# Na katere podprobleme se direktno skicuje rekurzivna definicija fib?

# Definirajte fib ki gradi rezultat od spodaj navzgor (torej računa in si zapomni
# vrednosti od 1 proti n.)
def fib_memo_iter(n):
    i = 2
    a = [0,1]
    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2]) 
        i += 1
    return a[n]
# Izboljšajte prejšnjo različico tako, da hrani zgolj rezultate, ki jih v
# nadaljevanju nujno potrebuje.
def fib_iter(n):
    i = 1
    a =1
    b = 0
    while i < n:
        i+=1
        a, b = a+b, a
    return a
