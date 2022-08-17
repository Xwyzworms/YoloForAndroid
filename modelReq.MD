
## Model Explanation 
- Object detection For 
    - Cat
    - Dog

- Train Configuration 
    - imageSize : 416
    - batch : 16
    - Epochs : 60
    - weights : yolov5s.pt ( biar Size modelnya kecil :v)
    - Dataset Size : 100 Per class Approximately

- Train Result
    - mAP@50 : 0.9
    - mAP@95 : 0.56

- Validation Result : 
    - mAP@50 : 0.9
    - mAP@95 : 0.58

- Model converted into : 
    .tflite ( no quantisasition )

- How To deploy on Android ? 
    - Nanti Aku masukin

### More Result ? You can Check at
- runs Folder, Kalau nanti Train YOLO, hasilnya ada di yolov5/runs
