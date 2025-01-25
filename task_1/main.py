import os
import shutil
import argparse
from pathlib import Path

def create_test_files(base_dir):
    # Генерує тестову структуру директорій і файлів.
    temp_dir = Path(base_dir) / "temp"
    temp_dir.mkdir(parents=True, exist_ok=True)

    # Створення тестових файлів
    (temp_dir / "texts").mkdir(exist_ok=True)
    (temp_dir / "images").mkdir(exist_ok=True)

    (temp_dir / "texts" / "example1.txt").write_text("This is a text file.")
    (temp_dir / "texts" / "example2.csv").write_text("name,age\nJohn,30\n")
    (temp_dir / "images" / "image1.jpg").write_bytes(b"This is a JPEG image.")
    (temp_dir / "images" / "image2.png").write_bytes(b"This is a PNG image.")
    (temp_dir / "example.pdf").write_bytes(b"This is a PDF file.")
    (temp_dir / "example.docx").write_bytes(b"This is a DOCX file.")

    print(f"Тестові файли створено в папці: {temp_dir}")
    return temp_dir

def copy_and_sort_files(src, dest):
    # Рекурсивно копіює файли з сортуванням за розширеннями.
    src_path = Path(src)
    dest_path = Path(dest)

    if not src_path.exists():
        print(f"Вихідна директорія {src} не існує.")
        return

    dest_path.mkdir(parents=True, exist_ok=True)

    for item in src_path.iterdir():
        if item.is_dir():
            # Рекурсивно обробляємо піддиректорії
            copy_and_sort_files(item, dest_path)
        elif item.is_file():
            ext = item.suffix[1:] or "no_extension"
            target_dir = dest_path / ext
            target_dir.mkdir(exist_ok=True)

            try:
                shutil.copy2(item, target_dir / item.name)
                print(f"Копіюється {item} до {target_dir / item.name}")
            except Exception as e:
                print(f"Помилка копіювання {item}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Копіювання та сортування файлів за розширенням.")
    parser.add_argument("src", nargs="?", help="Вихідна директорія", default=None)
    parser.add_argument("dest", nargs="?", help="Директорія призначення", default="dist")
    args = parser.parse_args()

    if args.src is None:
        print("Оберіть опцію:")
        print("1. Створити тестові файли у папці 'temp'.")
        print("2. Використати існуючу директорію.")
        choice = input("Ваш вибір (1/2): ").strip()

        if choice == "1":
            temp_dir = create_test_files("test_environment")
            copy_and_sort_files(temp_dir, args.dest)
        elif choice == "2":
            src = input("Введіть шлях до існуючої директорії: ").strip()
            copy_and_sort_files(src, args.dest)
        else:
            print("Невірний вибір. Завершення програми.")
    else:
        copy_and_sort_files(args.src, args.dest)

if __name__ == "__main__":
    main()