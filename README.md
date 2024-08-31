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
~~~
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
~~~

## How to run the training script
1. git clone the repo
2. Go to the initScripts folder and run the trainingScript.ipynb file
3. After all cells have been ran, model should be exported into tensorrt format in the ./runs/classify/trainX/weights folder, under the name best.engine

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

The outputted result should look something like this:

![results sample](https://github.com/user-attachments/assets/098b75d3-c1f5-474b-a226-eab94e388201)

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




