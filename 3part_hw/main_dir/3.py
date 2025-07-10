import sys
from pathlib import Path

from colorama import init, Fore
init(autoreset=True)

def print_tree(directory: Path, prefix: str = ""):
    try:
        for item in directory.iterdir():
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}/")
                print_tree(item, prefix + "    ")
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}Немає доступу до > {directory}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Ви не вказали шлях до директорії.")
        print(f"{Fore.YELLOW}Використання: python tree_view.py /шлях/до/текі")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Шлях не існує: {path}")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Це не директорія: {path}")
        return

    #print(f"{Fore.CYAN}Структура директорії > {path}\n")
    print_tree(path)

if __name__ == "__main__":
    main()

# python3 3.py "/Users/cyber/Desktop/VS PROJECTS/goit-pycore-hw-04/3part_hw/main_dir"

