import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
 
 
if __name__ == '__main__':
    model = YOLO('runs/train/plantdoc_exp8/weights/best.pt')
    model.predict(source='images/bus.jpg',
                  imgsz=640,
                  project='runs/detect',
                  name='exp',
                  save=True,
                )