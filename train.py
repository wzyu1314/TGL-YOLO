import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r'ultralytics\cfg\models\v5\yolov5.yaml')
    model.train(
                data='datasets/PlantDoc/data.yaml',
                cache=False,
                imgsz=640,
                epochs=10,
                batch=16, 
                workers=0, 
                project='runs/train',
                name='yolov5_exp',
                )
    