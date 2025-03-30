from string import ascii_lowercase, ascii_uppercase
from random import choice

def password_generator():
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        password = ''.join(choice(chars) for _ in range(12))
        yield password

# Создаем генератор
gen = password_generator()

# Выводим первые 5 паролей
print("Первые 5 сгенерированных паролей:")
for i in range(5):
    print(f"{i+1}. {next(gen)}")