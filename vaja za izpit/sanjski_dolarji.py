denominations = [1, 4, 7, 13, 28, 52, 91, 365]

def najvecji_bankovec_manjsi_od_n(sez, n):
    sez = sez[::-1]
    for i in range(0, len(sez)+1):
        if sez[i] <= n:
            return sez[i]   
        else:
            i += 1
      
def bills_greedy(n):
    seznam = []
    while n>0:
        seznam = seznam + [najvecji_bankovec_manjsi_od_n(denominations, n)]
        n = n - najvecji_bankovec_manjsi_od_n(denominations, n)
    return seznam



