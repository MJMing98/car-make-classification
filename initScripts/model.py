from ultralytics import YOLO

def train(datasetPath) -> dict:
    
    # Load model and get benchmark training metrics
    model = YOLO('yolov8n-cls.pt')    
    metrics_benchmark = model.train(data = datasetPath, epochs = 5, device = [0])

    # Now run with hyperparameter training for increased performance, ultralytics uses genetic algo for fine tuning
    metrics_aftertune = model.tune(data = datasetPath, epochs = 20, iterations = 15)

    return metrics_benchmark, metrics_aftertune, model
    
    
    