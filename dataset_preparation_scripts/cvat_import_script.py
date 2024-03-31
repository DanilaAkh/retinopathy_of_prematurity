import os


with open("./first_dataset/tags.txt", "w") as f:    
    for image in os.listdir("./first_dataset/healthy"):
        f.write(f"{image} 0\n")
    for image in os.listdir("./first_dataset/unhealthy"):
        f.write(f"{image} 1\n")

with open("./second_dataset/tags.txt", "w") as f:    
    for image in os.listdir("./second_dataset/healthy"):
        f.write(f"{image} 0\n")
    for image in os.listdir("./second_dataset/stage 2-3"):
        f.write(f"{image} 1\n")
    for image in os.listdir("./second_dataset/plus"):
        f.write(f"{image} 2\n")