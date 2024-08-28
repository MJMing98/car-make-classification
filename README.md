# Car make classification
Classification of car make images

This project performs the following:
1. Splits raw image data into train and test splits
2. Runs a basic primitive training process of an ultralytics YOLOv8 image classifier object with the split data
3. Performs hyperparameter training using ultralytics' genetic algorithm approach, which mainly utilizes the Mutation concept, in essence introducing minimal random parameter changes during backpropagation for non-linear error minimization progression
4. Performs inference on a random image for each respective label and displays the inference scores in image format
5. Exports the ultralytics' YOLOv8 model in the form of an tensorrt engine

## Note:
Run this command to download cuda compatible pytorch:
'''
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
'''
