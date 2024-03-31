import os
import shutil


# Распределение фотографий из папки Anon по first_dataset
for dir_name in os.listdir('.\\Anon'):
    if dir_name[-1] == "N":
        for image in os.listdir(f"./Anon/{dir_name}"):
            shutil.copy(f"./Anon/{dir_name}/{image}", f"./first_dataset/healthy/{image}")
    else:
        for image in os.listdir(f"./Anon/{dir_name}"):
            if image[image.rfind(".") + 1:] in ["jpg"]:
                shutil.copy(f"./Anon/{dir_name}/{image}", f"./first_dataset/unhealthy/{image}")


# Распределение фотографий из папки Anon по second_dataset
for dir_name in os.listdir('.\\Anon'):
    if (dir_name[-1] == "2" or dir_name[-1] == "3") and dir_name[-1] != "N":
        for image in os.listdir(f"./Anon/{dir_name}"):
            if image[image.rfind(".") + 1:] in ["jpg"]:
                shutil.copy(f"./Anon/{dir_name}/{image}", f"./second_dataset/stage 2-3/{image}")
    elif dir_name[-1] == "N":
        for image in os.listdir(f"./Anon/{dir_name}"):
            shutil.copy(f"./Anon/{dir_name}/{image}", f"./second_dataset/healthy/{image}")
    elif "plus" in (dir_name.lower()):
        for image in os.listdir(f"./Anon/{dir_name}"):
            shutil.copy(f"./Anon/{dir_name}/{image}", f"./second_dataset/plus/{image}")