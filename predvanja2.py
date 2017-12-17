import pandas as pd #ne rabimo označevati vsakič pandas
#searies--ime stolpca
#serije.head/.tail
#serije['ime']
#serije[(serije['leto_zacetka']== 2003) & (serije[ocena] > 8.5)].sort_values('dolzina')
#grupiranje:
#serje.groupby('leto_zacetka').count() ali .size() , .mean()...povprečje
#ali se ocena v povprečju izboljšuje ali ne:
# .mean(()['ocena']
#na 5 let: 5 * (serije['leto_zacetka'] -2//5) +2
#graf:
#%matplotlib inline
serije = pd.read_csv('serije.csv', index_col = 'id')
serije.plot.scatter( , ) # točkovni graf
plot.bar #za diskretne, kategorične spremenljivke

##############################
#NAIVNI BAYESOV KLASIFIKATOR
##############################
span: izračuna verjetnost, da je span, na podlagi besed
serija je nekega žanra na podlagi opisa
bayesov izrek: P(A presek B) = P(A) * P(B|A)
P(serija žanra Ž|opis vsebuje besede b1, b2...bn)
predpostavimo, da so besede med sabo neodvisne --> zato naivni
P(b1|Ž) * P(b2|Ž)***P(bn|Ž)*P(Ž) / P(b1 ^...^bn)
zanima nas le, kje je ta verj največja, zato lahko imenovalec pozabimo (povsod enak)

--Avtomatično določanje žanrov
verj_korena_pri_zanru.index.isin(['', ''])
