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

(The original PlantDoc dataset can be found [here](https://github.com/pratikkayal/PlantDoc-Dataset).)

---

## 🧠 Custom Modules Location

The custom modules implemented in this paper can be found at the following paths:

* **`ultralytics/nn/modules/block.py`**: Contains the source code for `TSDBlock`, `GPST`, and `LSPA`.
* **`ultralytics/cfg/models/11/yolo11-tgl.yaml`**: The model configuration file for defining the architecture and training parameters of TGL-YOLO.

---

## 🏃‍♂️ Reproducibility: Training & Inference

To ensure complete reproducibility of our empirical results, please follow the pipelines below.

### 1. Train from Scratch

To reproduce the training process on the PlantDoc dataset using the same conditions reported in our manuscript:

```bash
python train.py --cfg ultralytics/cfg/models/11/yolo11-tgl.yaml --data datasets/PlantDoc/data.yaml --epochs 200 --batch-size 16 --imgsz 640 --device 0
```

*(Note: Please adjust the `--batch-size` according to your GPU memory limits. ).*

### 2. Validation (Verify Reported mAP)

To verify the exact `mAP@0.5` metrics, run the validation script using the weights generated after training:

```bash
python val.py --weights runs/train/exp/weights/best.pt --data datasets/PlantDoc/data.yaml --imgsz 640 --task test
```

### 3. Inference / Visualization

To generate bounding box predictions on your own images:
```bash
python predict.py --weights runs/train/exp/weights/best.pt --source your_image_folder/ --conf 0.25
```