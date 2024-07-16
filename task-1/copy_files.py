import os
import shutil
import sys

def copy_files_recursively(src_dir, dst_dir):
    try:
        # Перебір елементів у вихідній директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                # Якщо елемент є директорією, викликаємо функцію рекурсивно
                copy_files_recursively(src_path, dst_dir)
            else:
                # Якщо елемент є файлом, копіюємо його до нової директорії
                file_ext = os.path.splitext(item)[1][1:]  # Отримуємо розширення файлу без крапки
                ext_dir = os.path.join(dst_dir, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)  # Створюємо директорію для розширення файлу, якщо вона не існує
                
                dst_path = os.path.join(ext_dir, item)
                
                # Якщо файл з таким ім'ям вже існує, створюємо нове ім'я
                if os.path.exists(dst_path):
                    base_name, extension = os.path.splitext(item)
                    counter = 1
                    new_name = f"{base_name}_{counter}{extension}"
                    new_dst_path = os.path.join(ext_dir, new_name)
                    while os.path.exists(new_dst_path):
                        counter += 1
                        new_name = f"{base_name}_{counter}{extension}"
                        new_dst_path = os.path.join(ext_dir, new_name)
                    dst_path = new_dst_path
                
                shutil.copy2(src_path, dst_path)  # Копіюємо файл
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    # Парсинг аргументів командного рядка
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<destination_directory>]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        sys.exit(1)

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)  # Створюємо директорію призначення, якщо вона не існує

    # Виклик функції для копіювання файлів
    copy_files_recursively(src_dir, dst_dir)

if __name__ == "__main__":
    main()

