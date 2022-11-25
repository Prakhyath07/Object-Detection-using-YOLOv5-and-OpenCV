# Object Detection using YOLOv5 and OpenCV DNN (C++/Python)

**This repository contains the code for [Object Detection using YOLOv5 and OpenCV DNN in C++ and Python](https://learnopencv.com/object-detection-using-yolov5-and-opencv-dnn-in-c-and-python/) blogpost**.


<img src="https://learnopencv.com/wp-content/uploads/2022/04/yolov5-feature-image.gif" alt="Introduction to YOLOv5 with OpenCV DNN" width="950">

## Install Dependancies

[<img src="https://learnopencv.com/wp-content/uploads/2022/07/download-button-e1657285155454.png" alt="download" width="200">](https://www.dropbox.com/sh/f41c0c6hvdw25ws/AABb2gk5SdkYLPopkz-u3dzia?dl=1)

```
pip install -r requirements.txt
```
List of tutorials for installing OpenCV for C++ [here](https://learnopencv.com/category/install/).


## Execution
### Python
```Python
python yolov5.py
```
### CMake C++ Linux
```C++ Linux
mkdir build
cd build
cmake ..
cmake --build .
./main
```
### CMake C++ Windows
```C++ Windows
rmdir /s /q build
cmake -S . -B build
cmake --build build --config Release
.\build\Release\main.exe
```

# AI Courses by OpenCV

Want to become an expert in AI? [AI Courses by OpenCV](https://opencv.org/courses/) is a great place to start. 

<a href="https://opencv.org/courses/" target="_blank">
<p align="center"> 
<img src="https://www.learnopencv.com/wp-content/uploads/2020/04/AI-Courses-By-OpenCV-Github.png">
</p>
</a>


"""
Steps to convert .pt to .onnx so that opencv can load it
# Clone the repository. 
!git clone https://github.com/ultralytics/YOLOv5
 
%cd YOLOv5 # Install dependencies.
!pip install -r requirements.txt
!pip install onnx
 
# Download .pt model.
!wget https://github.com/ultralytics/YOLOv5/releases/download/v6.1/YOLOv5s.pt
 
%cd .. # Export to ONNX.
!python export.py --weights models/YOLOv5s.pt --include onnx
 
# Download the file.
from google.colab import files
files.download('models/YOLOv5s.onnx')

"""