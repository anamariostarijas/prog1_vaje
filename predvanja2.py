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