import random

def random_gumik():
    gyumik = ["alma" , "körte", "szilva", "barack", "málna", "füge", "eper"]
    return [random.choice(gyumik) for _ in range(30)]

print(random_gumik())