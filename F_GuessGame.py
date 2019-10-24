import random
import json
import datetime
from operator import itemgetter


def play_game_easy():
    secret = random.randint(1, 5)
    attempts = 0
    score_list = get_score_list()
    wrong_guesses = []

    while True:
        guess = int(input("Guess the secret number (between 1 and 5): "))
        attempts += 1

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))

            current_time = str(datetime.datetime.now())
            user = input("¿Usuario?")
            score_data = {"attempts": attempts, "date": current_time, "nombre": user, "Wrong_guesses": wrong_guesses}
            score_list.append(score_data)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)


def play_game_hard():
    secret = random.randint(1, 5)
    attempts = 0
    score_list = get_score_list()
    wrong_guesses = []

    while True:
        guess = int(input("Guess the secret number (between 1 and 5): "))
        attempts += 1

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))

            current_time = str(datetime.datetime.now())
            user = input("¿Usuario?")
            score_data = {"attempts": attempts, "date": current_time, "nombre": user, "Wrong_guesses": wrong_guesses}
            score_list.append(score_data)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break

    wrong_guesses.append(guess)

def get_top_scores():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

        lista_top = sorted(score_list, key=itemgetter("attempts"))[:3]
        for x in lista_top:
            print(str(x["attempts"]) + " attempts, " + x["nombre"])


def get_score_list():
    import json
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


while True:
    selection = input("¿Qué quieres hacer?: 1) Jugar 2) Ver la mejor puntuación 3) Salir")
    if selection == "1":
        nivel = input("Nivel: A) Difícil B) Fácil")

        if nivel.upper() == "A":
            play_game_hard()
        else:
            play_game_easy()

    elif selection == "2":
        get_top_scores()
    else:
        break