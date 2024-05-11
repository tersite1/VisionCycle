

# VisionCycle : Auto Labeling Pipeline using Neural Radience Field


<p align="center">
  <img src="https://github.com/tersite1/tersite1/assets/160453556/41c721bf-ab38-4264-a3e0-23388e62fcc1">
</p>




## Introduction
VisionCycle leverages Neural Radiance Fields (NeRF) to automate labeling processes for machine learning. It reconstructs a small number of 2D images into 3D using Instant NGP, renders the models from various angles to obtain new views, and automatically creates bounding boxes for YOLO training.


<br>
<br>



## Pipeline Process
1. **2D to 3D Reconstruction**: Convert 2D photos to 3D models using Instant NGP.
2. **3D to 2D Rendering**: Render 3D models from various angles to produce new 2D images.
3. **Bounding Box Creation**: Auto-generate bounding boxes on the new 2D images.
4. **YOLO Training**: Use the images for machine learning model training.

<img width="1024" alt="스크린샷 2024-05-11 오후 10 32 06" src="https://github.com/tersite1/tersite1/assets/160453556/0b7cc713-7b17-4ba5-abbe-d7631e7e136d">

<br>
<br>




## Components Description
- **`NeRF.py`**: Executes Instant NGP to transform 2D images into 3D models.
- **`AutoCapture.py`**: Manages the rendering of 3D models into 2D views.
- **`AutoBounding.py`**: Automates bounding box creation in the new 2D images.



<br>
<br>


## Used Papers
- Gao, J., Shen, T., Wang, Z., Chen, W., Yin, K., Li, D., Litany, O., Gojcic, Z. and Fidler, S., 2022. Get3d: A generative model of high quality 3d textured shapes learned from images. Advances In Neural Information Processing Systems, 35, pp.31841-31854.
- Müller, T., Evans, A., Schied, C. and Keller, A., 2022. Instant neural graphics primitives with a multiresolution hash encoding. ACM Transactions on Graphics (TOG), 41(4), pp.1-15.

<br>
<br>

## Dependencies
Required Python packages:
- TensorFlow
- PyTorch
- OpenCV
- bpy
- pillow
- numpy
- OpenGL
- CUDA (if it possbile)

#### CUDA Installation

For improved performance, install CUDA to enable GPU acceleration. Please follow the official [CUDA Installation Guide](https://developer.nvidia.com/cuda-downloads) to download and install CUDA suitable for your system.




#### Install dependencies:

```bash
pip install -r requirements.txt
```
<br>



## Installation
```
git clone https://github.com/tersite1/VisionCycle.git
cd VisionCycle
pip install -r requirements.txt
```

<br>


## Usage

```
python3 main.py 'path_to_dataset'
```
<br>



## Contact
- Minsuk Jang - itcouldbe0@yonsei.ac.kr


## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgement

-  Support and funding from Yonsei University
-  Resources provided by NVIDIA





