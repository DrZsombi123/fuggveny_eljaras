import random

def random_gumik(hossz):
    gyumik = ["alma" , "körte", "szilva", "barack", "málna", "füge", "eper"]
    return [random.choice(gyumik) for _ in range(hossz)]

print(random_gumik(5))