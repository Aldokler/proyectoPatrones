import os

path = "dataset/"

dataset = os.listdir(path+"train")

with open(path+"train.txt", 'w') as f:
    for i in dataset:
        f.write("train/"+i+'\n')

validation = os.listdir(path+"valid")

with open(path+"val.txt", 'w') as f:
    for i in validation:
        f.write("valid/"+i+'\n')

print("Redy")