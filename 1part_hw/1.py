from pathlib import Path
import re

path = Path(__file__).parent / "my specialists.txt"

def total_salary(path):
    try:
        with open(path, "r") as salary:
            salary_list = []
            for sal in salary:
                digits = re.findall(r"\d+", sal)
                digit = int("".join(digits))
                salary_list.append(digit)
            total = sum(salary_list)
            averege = total / len(salary_list)
        return total, int(averege)
    except:
        return None

if total_salary(path) is None:
    print("Перевірте коректність файлу")
else:
    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

            
