import random
import time
print("Добро пожаловать в игру на скорость реакции!")
number = int(input("Сколько чисел вы хотите ввести на время?"))
mistakes = 0
schetchik = 0
print("\nПриготовтесь........")
time.sleep(random.randint(1,3))
print("СТАРТ!\n")
start = time.time()
while schetchik < number:
    wish_number = random.randint(1, 9)  
    time_before_input = time.time()
    print("Как можно быстрее введите число:", wish_number)
    user_input = int(input("Ваш ответ: "))
    time_after_input = time.time()
    reaction_time = time_after_input - time_before_input
    if user_input != wish_number: 
        print("Ошибка! Неправильное число.")
        mistakes = mistakes + 1
    elif reaction_time > 1.5:
        print("Слишком медленно! Вы думали", round(reaction_time, 2), "сек. (Лимит: 1.5 сек.)")
        mistakes = mistakes + 1
    else:
        print("Успешно! Время:", round(reaction_time, 2), "сек.")    
    schetchik = schetchik + 1
end = time.time()
general_time = round(end - start, 2)
print("\nИГРА ОКОНЧЕНА")
print("Вы справились за", general_time, "секунд!") 
print("Сделано ошибок (или не успел по времени):", mistakes)
