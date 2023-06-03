import os
import shutil
import random

dataset_path = '/content/dataset'  
train_path = '/content/train'
validation_path = '/content/validation'
test_path = '/content/test'

train_ratio = 0.7
validation_ratio = 0.15
test_ratio = 0.15

os.makedirs(train_path, exist_ok=True)
os.makedirs(validation_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

for class_name in os.listdir(dataset_path):
    class_dir = os.path.join(dataset_path, class_name)
    if not os.path.isdir(class_dir):
        continue

    train_class_path = os.path.join(train_path, class_name)
    validation_class_path = os.path.join(validation_path, class_name)
    test_class_path = os.path.join(test_path, class_name)

    os.makedirs(train_class_path, exist_ok=True)
    os.makedirs(validation_class_path, exist_ok=True)
    os.makedirs(test_class_path, exist_ok=True)

    for filename in os.listdir(class_dir):
        if random.random() < train_ratio:
            shutil.copy(os.path.join(class_dir, filename), os.path.join(train_class_path, filename))
        elif random.random() < (train_ratio + validation_ratio):
            shutil.copy(os.path.join(class_dir, filename), os.path.join(validation_class_path, filename))
        else:
            shutil.copy(os.path.join(class_dir, filename), os.path.join(test_class_path, filename))
