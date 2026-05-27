import warnings

warnings.filterwarnings("ignore")
from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("runs/train/plantdoc_exp8/weights/best.pt")
    model.val(
        data="datasets/PlantDoc/data.yaml",
        split="test",  # 关键修改：使用测试集
        imgsz=640,
        batch=16,
        save_json=True,  # 建议开启以保存评估指标
        project="runs/test",
        name="plantdoc_exp",
    )
