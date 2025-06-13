# Функция открытия справки
import os
import subprocess

def open_help_file(e):
    help_file = "usermanual.chm"
    try:
        if os.path.exists(help_file):
            subprocess.Popen(["hh.exe", help_file], shell=True)
        else:
            print(f"Файл справки {help_file} не найден!")
    except Exception as ex:
        print(f"Ошибка при открытии файла справки: {ex}")

