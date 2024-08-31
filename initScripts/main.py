from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from data_splitter import random_image
import os
from cv2 import imdecode, IMREAD_COLOR
from numpy import frombuffer, uint8

# Create app and load model
imgPredictionApp = FastAPI()
model = YOLO(f'{os.path.dirname(os.getcwd())}\\runs\\classify\\train6\\weights\\best.engine', )

# Example file image used for default:
randTestImg = random_image(f'{os.getcwd()}\\data_split\\test\\toyota_vios\\')

# Deploy model in POST endpoint
@imgPredictionApp.post('/predict')
async def predict(imgFile: UploadFile = File(...)) -> dict:
    """
    Predicts the car make and model from an uploaded image.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        A dictionary containing the predicted car make and model.
    """

    # Read the image data
    image_data = await imgFile.read()

    # Perform object detection using YOLOv8
    image = frombuffer(image_data, dtype = uint8)
    image = imdecode(image, IMREAD_COLOR)
    results = model.predict(image)

    # Extract the predicted car make and model
    jsonResults = []
    for result in results:
        jsonResults.append({"image_name": imgFile.filename,
                            "image_class": result.names[result.probs.top1],
                            "image_probability": result.probs.top1conf.item()
                            })

    return {"results": jsonResults}