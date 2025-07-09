from pathlib import Path
from pprint import pprint

path = Path(__file__).parent / "cats.txt"

def get_cats_info(path):
    try:
        cats_list = []
        with open(path, "r", encoding="utf-8") as cats_file:       
            for cat in cats_file:
                cat = cat.strip()
                if not cat: # якщо немає строчки, переходжу до наступної ітерації
                    continue

                parts = cat.split(",") # розбиваю рядок на частини у список через кому
                cat_id, name, age = parts # розпаковую список задаючи змінним значення (майбутні значення ключів)
                
                cat_id = cat_id or "unknown" # обробляю випадок відсутності ID кота
                name   = name or "unknown" # обробляю випадок відсутності імені кота

                try:
                    age = int(age)
                except ValueError:
                    age = "unknown" # перевіряю чи вік є числом

                cats_list.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })      
        return cats_list
    except:
        return None # обробляю випадок, коли файл не коректний

cats_info = get_cats_info(path)

if cats_info:
    pprint(cats_info) # виводжу кожен словник з нового рядку за допомогою модулю pprint
else:
    print("Перевірте правильність файлу")

# усі рішення з виведенням списку словників з нового рядку загромоджували код і я знайшов модуль pprint та заюзав його тут