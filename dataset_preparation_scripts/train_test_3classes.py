import os
from random import shuffle
import shutil

# for dir in os.listdir("./second_dataset"):
#     for image in os.listdir(f"./second_dataset/{dir}"):
#         shutil.copy(f"./second_dataset/{dir}/{image}", f"./annotations/images/{image}")


jpg_files = [file for file in os.listdir("./annotations/images") if file.lower().endswith('.jpg')]
shuffle(jpg_files)

total_files = len(jpg_files)
trainval_count = int(0.7 * total_files)
test_count = int(0.2 * total_files)
valid_count = total_files - trainval_count - test_count

trainval_files = jpg_files[:trainval_count]
test_files = jpg_files[trainval_count:trainval_count + test_count]
valid_files = jpg_files[trainval_count + test_count:]

# Функция для записи списка файлов в файл
def write_to_file(file_list, filename):
    with open(filename, 'w') as f:
        for file in file_list:
            for dir in os.listdir("./second_dataset"):
                for image in os.listdir(f"./second_dataset/{dir}"):
                    if image == file and dir == "healthy":
                        f.write(file+",0\n")
                    elif image == file and dir == "stage 2-3":                        
                        f.write(file+",1\n")
                    elif image == file and dir == "plus":                        
                        f.write(file+",2\n")

# Записываем списки в соответствующие файлы
write_to_file(trainval_files, './annotations/train_3classes.txt')
write_to_file(test_files, './annotations/test_3classes.txt')
write_to_file(valid_files, './annotations/valid_3classes.txt')