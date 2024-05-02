from collections import deque

def is_palindrome(str):
    # видалення пробілів і перевод в нижній регістр
    clean_str = ''.join(c.lower() for c in str if c.isalnum())

    # Створєння двосторонньої черги
    new_deque = deque(clean_str)

    while len(new_deque) > 1:
        if new_deque.popleft() != new_deque.pop():
            return False
        
    return True


test_strings = [
    "Tammat",               # парна кількість символів
    "No lemon no melon",    # непарна
    "Hello World",          # не паліндром
]

for string in test_strings:
    print(f"'{string}' є паліндромом? {is_palindrome(string)}")