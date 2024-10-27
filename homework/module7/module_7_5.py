import os
import time

def file_info(directory):
    for  root, dirs, files in os.walk(directory): # для обхода каталога, путь к которому указывает переменная directory
        for file in files:
            filepath = os.path.join(root,file) # абсолютный путь. в windows начинается с диска, например с C:\
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(filepath))) # для получения и отображения времени последнего изменения файла
            filesize = os.path.getsize(filepath) # для получения размера файла
            parent_dir = os.path.dirname(filepath) # для получения родительской директории файла
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


directory=r'C:\python\PyProjectsForStudy\homework\module7'
file_info(directory)







