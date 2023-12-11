import random
import sys
while True:
    print("Угадайте число")
    num=random.randint(1, 5)
    a=0
    attempts = 5
    while a==0:
     answer = int(input())
     if answer == num:
        print("Победа")
        a=1
     elif answer > num:
        print("Ответ меньше")
        attempts -=1
     elif answer < num:
        attempts -= 1
        print("Ответ больше")
     if attempts == 0:
        print("Поражение")
        a=1
     if attempts == 0 or answer == num:
        print("Do you wanna play again? y/n")
        p = input()
        if p == "n":
            print("Игра окончена")
            sys.exit ()
        else:
            continue






