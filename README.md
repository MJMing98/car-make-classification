# Car make classification
Classification of car make images

This project performs the following:
1. Splits raw image data into train and test splits
2. Runs a basic primitive training process of an ultralytics YOLOv8 image classifier object with the split data
3. Performs hyperparameter training using ultralytics' genetic algorithm approach, which mainly utilizes the Mutation concept, in essence introducing minimal random parameter changes during backpropagation for non-linear error minimization progression
4. Performs inference on a random image for each respective label and displays the inference scores in image format
5. Exports the ultralytics' YOLOv8 model in the form of an tensorrt engine

## Tasks completed:
| Task | Comments |
| ---------- | ---------- |
| Dataset Preparation | Done and succesfully split according to Ultralytic's Yolov8 format |
| Environment Setup | Done locally as I have a GPU, not through Google Colab |
| Model Training | Done, hyperparameter tuning done using Ultralytic's tune function which uses genetic algorithm for finetuning the model but no preprocessing steps added |
| Inference | Done with results displayed |
| Convert the Trained Model to TensorRT (INT8 Precision) | Calibration not done as original plan was to complete everything first and then play around more with better finetuning/preprocessing steps, but model succesfully exported to TensorRT format |
| Push Your Code to GitHub | Done for parts/code that were successful |
| Deploy the Model Using FastAPI | Done with API documented using OpenAPI |
| Write a Dockerfile and Build a Docker Image | Dockerfile created, but image keeps failing and therefore not pushed to Docker Hub account |
| Deliverables: | Everything done (Github repo, FastAPI instructions) except for link for Docker Hub repo link |


## Note:
Run this command to download cuda compatible pytorch:
~~~
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
~~~

## How to run the training script
1. git clone the repo
2. Go to the initScripts folder and run the trainingScript.ipynb file
3. After all cells have been ran, model should be exported into tensorrt format in the ./runs/classify/trainX/weights folder, under the name best.engine

## Results of procured images
Below is an example image showing the inference after an image has been classified:
![results sample](https://github.com/user-attachments/assets/098b75d3-c1f5-474b-a226-eab94e388201)

Here are some displayed images obtained from the trainingScript.ipynb file:
![sample axia](https://github.com/user-attachments/assets/bfab8335-58c2-43b7-a0e8-60612d1eb281)  
**Caption:** Perodua Axia example image with confidence score displayed on top left

![sample vios](https://github.com/user-attachments/assets/0e003d56-b0aa-4867-b9e9-6d14ff5be8a7)  
**Caption:** Toyota Vios example image with confidence score displayed on top left

## Deployment of the model itself
1. After training script has been ran, change the main.py file's model variable value to the path for the procured tensorrt engine file (file format should be in *.engine)
2. Run the following command on the terminal:
~~~
uvicorn main:imgPredictionApp --reload
~~~
3. Open postman, create a **POST** request for endpoint http://localhost:8000/predict and add the below settings:

| Properties | Values |
| ---------- | ---------- |
| Content-type (Headers) | multipart/form-data |
| imgFile | < Insert path to file here in value column > |

## How to build the dockerfile
1. At the main directory, run the following command to create the image (imgfile name can be changed to something else, depending on user):
~~~
docker build -t <insert image name> .
~~~
2. Once build is complete, we can then start the container by running the image file by doing:
~~~
docker run -dp 127.0.0.1:8000:8000 <insert image name>
~~~
3. Go back to postman and rerun the request without uvicorn running in the background, and the response should be returned




