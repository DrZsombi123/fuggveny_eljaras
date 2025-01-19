def osszead(szam1, szam2):
    if szam1>szam2:
        print("A nagyobb szám az első szám: ", szam1)
    elif szam1<szam2:
        print("A nagyobb szám a második szám: ", szam2)
    else:
        print("A két szám egyenlő", szam1,"=", szam2)

osszead(1,2)