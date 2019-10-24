import random

juego = {"España": "Madrid",  "Francia": "Paris", "Italia": "Roma", "Alemania": "Berlin"}

b = random.choice(list(juego))

pregunta = input(str("Cuál es la capital de " + str(b) + "?"))

a = juego[b]


if pregunta.capitalize() == juego[b]:
   print("Genial, has acertado!")

else:
    print("Oh, no has acertado")


