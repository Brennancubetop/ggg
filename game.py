import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуйте угадать!")

    while True:
        try:
            guess = int(input("Введите ваше: "))
            attempts += 1

            if guess < number:
                print("Загаданное число больше.")
            elif guess > number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {number} за {attempts} попыток.")
                break
        except ValueError:
            print("Ошибка! Введите целое число.")

if __name__ == "__main__":
    guess_the_number()
