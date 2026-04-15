## 🛠️ Installation & Requirements

**1. Clone the repository:**
```bash
git clone https://github.com/wzyu1314/TGL-YOLO/TGL-YOLO.git
cd TGL-YOLO
```

**2. Install dependencies:**
We recommend using Python 3.10 and PyTorch 2.3.0
```bash
pip install -r requirements.txt
```

---

## 📁 Dataset Preparation

Our experiments are conducted on the public **PlantDoc** and **FieldPlant** datasets. Please organize your dataset directories following the standard YOLO format:

```text
datasets/
├── PlantDoc/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│   └── data.yaml
```


---

## 🧠 Custom Modules Implementation

For researchers wishing to independently verify our architectural choices, the custom modules described in the paper are implemented natively. You can locate them at:
* **`models/common.py`**: Contains the source code for `TSDBlock`, `GPST`, and `LSPA`.
* **`ultralytics/cfg/models/11/yolo11-tgl.yaml`**: The structural definition of the TGL-YOLO computational graph.

---

## 🏃‍♂️ Reproducibility: Training & Inference

To ensure complete reproducibility of our empirical results, please follow the pipelines below.

### 1. Train from Scratch

To reproduce the training process on the PlantDoc dataset using the same conditions reported in our manuscript:

```bash
python train.py --cfg ultralytics/cfg/models/11/yolo11-tgl.yaml --data datasets/PlantDoc/data.yaml --epochs 300 --batch-size 16 --imgsz 640 --device 0
```

*(Note: Please adjust the `--batch-size` according to your GPU memory limits. Our original experiments were conducted on a single NVIDIA RTX 3090).*

### 2. Validation (Verify Reported mAP)

To verify the exact `mAP@0.5` metrics, run the validation script using the weights generated after training:

```bash
python val.py --weights runs/train/exp/weights/best.pt --data datasets/PlantDoc/data.yaml --imgsz 640 --task test
```

### 3. Inference / Visualization

To generate bounding box predictions or SS-Grad-CAM++ heatmaps on your own images:

```bash
python predict.py --weights runs/train/exp/weights/best.pt --source your_image_folder/ --conf 0.25
```