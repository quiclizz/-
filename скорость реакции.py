import random
import time
print("----Добро пожаловать в игру на скорость реакции!----")
number = int(input("Сколько чисел вы хотите ввести на время? "))
mistakes = 0
schetchik = 0
print("\nПриготовтесь........")
time.sleep(random.uniform(1.5, 3.5)) 
print("СТАРТ!\n")
start = time.time()
while schetchik < number:
    wish_number = random.randint(1, 9)  
    time_before_input = time.time()
    user_input = int(input(f"Как можно быстрее введи число {wish_number}: "))
    time_after_input = time.time()
    reaction_time = time_after_input - time_before_input
    if user_input != wish_number: 
        print("Ошибка! Неправильное число.")
        mistakes = mistakes + 1
    elif reaction_time > 1.5:
        print(f"Слишком медленно! Ты думал {round(reaction_time, 2)} сек. (Лимит: 1.5 сек.)")
        mistakes = mistakes + 1
    else:
        print(f"Успешно! Время: {round(reaction_time, 2)} сек.")    
    schetchik = schetchik + 1
end = time.time()
general_time = round(end - start, 2)
print("\n----ИГРА ОКОНЧЕНА----")
print("Ты справился за", general_time, "секунд!") 
print("Сделано ошибок (или не успел по времени):", mistakes)
