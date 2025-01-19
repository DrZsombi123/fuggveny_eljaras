def kerulet(kotelezo, *opcionalis):
    if len(opcionalis) == 0:
        return f"Négyzet kerulete: {4 * kotelezo}"
    elif len(opcionalis) == 1:
        return f"Téglalap kerület: {2*(kotelezo + opcionalis[0])}"
    elif len(opcionalis) == 2:
        return f"Háromszög kerület: {kotelezo + opcionalis[0] + opcionalis[1]}"
    else:
        return f"Sokszög kerület: {sum(opcionalis) + kotelezo}"
print(kerulet(6))
print(kerulet(6, 8))
print(kerulet(6, 8, 10))
print(kerulet(6, 8, 10, 12))