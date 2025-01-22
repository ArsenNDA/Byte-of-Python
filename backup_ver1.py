import os
import time
import shutil

# Исходные файлы или директории для резервного копирования
source = ["/path/to/source1", "/path/to/source2"]

# Целевая директория для хранения резервных копий
target_dir = "/path/to/backup"


def make_backup(source, target_dir):
    try:
        # Проверяем, существует ли целевая директория, и создаём, если нет
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Формируем папку с временной меткой
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        backup_folder = os.path.join(target_dir, f"backup-{timestamp}")
        os.makedirs(backup_folder)

        # Копируем каждый элемент из списка источников
        for item in source:
            if os.path.exists(item):
                # Копируем файлы или папки
                if os.path.isdir(item):
                    shutil.copytree(item, os.path.join(backup_folder, os.path.basename(item)))
                else:
                    shutil.copy(item, backup_folder)
                print(f"Резервная копия {item} успешно создана.")
            else:
                print(f"Источник не найден: {item}")

        print(f"Резервная копия завершена. Все файлы сохранены в: {backup_folder}")
    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")


# Запуск
make_backup(source, target_dir)