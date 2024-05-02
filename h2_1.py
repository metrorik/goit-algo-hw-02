from queue import Queue
import random

# Створити чергу заявок
queue = Queue()

def generate_request():
    # Створити нову заявку
    new_application = random.randint(1, 100)
    print(f"Створена Заявка №{new_application}\n")
    # Додати заявку до черги
    queue.put(new_application)

def process_request():
    # Якщо черга не пуста:
    if not queue.empty():
        #     Видалити заявку з черги
        request = queue.get()
        #     Обробити заявку
        print(f"Обробляється Заявка № {request}\n")
    else:
        #     Вивести повідомлення, що черга пуста
        print("Черга пуста\n")


# Головний цикл програми:
while True:    
    #     Поки користувач не вийде з програми:
    action = input("'a' - додати заявку, 'p' - обробити заявку, 'q' - виход: ")
    #         Виконати generate_request() для створення нових заявок
    if action.lower() == 'a':
        generate_request()
    #         Виконати process_request() для обробки заявок
    elif action.lower() == 'p':
        process_request()
    elif action.lower() == 'q':
        break
    else:
        print("Невідома команда\n")
        
