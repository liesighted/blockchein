import hashlib
import itertools

iin = "050429502050"     # <-- здесь 12-значный ИИН


prefix = "00" # для двух нулей;
prefix2 = "000"

# Перебираем числа, пока не найдём подходящий результат
for counter in itertools.count():              # 0, 1, 2, 3, ...
    candidate = f"{iin}+{counter}"              # строка "ИИН+число"
    hash_hex = hashlib.sha256(candidate.encode()).hexdigest()
    if hash_hex.startswith(prefix):
        print("Найдено подходящее значение!")
        print("Входные данные :", candidate)
        print("SHA-256 хэш    :", hash_hex)
        break
for counter in itertools.count():              
    candidate = f"{iin}+{counter}"              
    hash_hex = hashlib.sha256(candidate.encode()).hexdigest()
    if hash_hex.startswith(prefix2):
        print("Найдено подходящее значение!")
        print("Входные данные :", candidate)
        print("SHA-256 хэш    :", hash_hex)
        break