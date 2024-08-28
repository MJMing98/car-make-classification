import os
import random
from shutil import copy

def splitData(rawDataPath) -> None:
    
    # Get car make folder paths    
    rawDataFolderPath = os.path.join(rawDataPath)
    carMakeFolders = [folder for folder in os.listdir(rawDataFolderPath) if os.path.isdir(os.path.join(rawDataFolderPath, folder))]
    
    # Define train and test split ratio
    train_ratio = 0.8

    # Create train and test folders
    train_folder, test_folder = os.path.join(os.getcwd(), 'data_split/train'), os.path.join(os.getcwd(), 'data_split/test')
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Iterate through each subfolder
    for subfolder in carMakeFolders:
        subfolder_path = os.path.join(rawDataFolderPath, subfolder)
        image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        # Shuffle image files randomly
        random.shuffle(image_files)

        # Calculate number of images for train and test sets
        num_train_images = int(len(image_files) * train_ratio)

        # Move images to train and test folders
        for i, image_file in enumerate(image_files):
            source_path = os.path.join(subfolder_path, image_file)
            if i < num_train_images:
                target_path = os.path.join(train_folder, subfolder, image_file)
            else:
                target_path = os.path.join(test_folder, subfolder, image_file)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            copy(source_path, target_path)

    print("Image data split into train and test sets.") 