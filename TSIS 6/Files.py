'''''''''''''''''''''''''''Task 1'''''''''''''''''''''''''''
import os
path = '.'
print(os.listdir())
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print(os.listdir(path))

'''''''''''''''''''''''''''Task 2'''''''''''''''''''''''''''
print(os.access(path,os.F_OK))
print(os.access(path,os.R_OK))
print(os.access(path,os.W_OK))
print(os.access(path,os.X_OK))

'''''''''''''''''''''''''''Task 3'''''''''''''''''''''''''''
if os.path.exists(path):
    print("Путь существует!")

    filename = os.path.basename(path)
    print("Имя файла:", filename)

    directory = os.path.dirname(path)
    print("Директория:", directory)
else:
    print("Путь не существует.")

'''''''''''''''''''''''''''Task 4'''''''''''''''''''''''''''
with open(filename, 'r', encoding='utf-8') as file:
        print(sum(1 for _ in file))

'''''''''''''''''''''''''''Task 5'''''''''''''''''''''''''''
my_list = ['a','s','d','fe','er','wf','w']
with open('task5.txt', 'w', encoding='utf-8') as file:
        for item in my_list:
            file.write(str(item) + '\n')

'''''''''''''''''''''''''''Task 6'''''''''''''''''''''''''''
import string
for letter in string.ascii_uppercase: 
    filename = f"{letter}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Это файл {filename}\n")

'''''''''''''''''''''''''''Task 7'''''''''''''''''''''''''''
with open('task5.txt', 'r', encoding='utf-8') as src, open('task7.txt', 'w', encoding='utf-8') as dest:
    dest.write(src.read())

'''''''''''''''''''''''''''Task 8'''''''''''''''''''''''''''
file_path = ''
if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("Файл удалён.")
    else:
        print("Нет доступа к файлу.")
else:
    print("Файл не существует.")