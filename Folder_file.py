import random


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.content = []


folder = Folder('My_folder', 20)

dinamic_size = 0

num = 1
while dinamic_size <= folder.size - 3:
    file = File(name=f'File_name-{num}', size=random.randint(1, 3))
    dinamic_size += file.size
    folder.content.append(file)
    num += 1

print(f'В папке {folder.name} {len(folder.content)} файлов суммарным размером {dinamic_size} Мб')
for el in folder.content:
    print(f'Файл - {el.name}, размер файла - {el.size} Мб')