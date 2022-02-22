import random


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder():
    def __init__(self, name, size):
        self.name = name
        self.size = size


folder = Folder('My_folder', 20)

Folder_content = []
Folder_list = []

num = 1
while sum(Folder_list) <= folder.size - 3:
    file = File(name=f'File_name-{num}', size=random.randint(1, 3))
    Folder_list.append(file.size)
    Folder_content.append(file)
    num += 1

print(f'В папке {folder.name} {len(Folder_content)} файлов суммарным размером {sum(Folder_list)} Мб')
for el in Folder_content:
    print(f'Файл - {el.name}, размер файла - {el.size} Мб')