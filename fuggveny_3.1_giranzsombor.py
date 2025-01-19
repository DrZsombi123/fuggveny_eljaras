def harommal_oszthatok():
    szamok=[1,2,3,4,5,6,7,8,9,10]
    oszthato_szamok=[]
    for szam in szamok:
        if szam % 3 == 0:
            oszthato_szamok.append(szam)
    return oszthato_szamok

print(harommal_oszthatok())