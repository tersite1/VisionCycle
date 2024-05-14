

# VisionCycle : Auto Labeling Pipeline using Neural Radience Field


<p align="center">
  <img src="https://github.com/tersite1/tersite1/assets/160453556/41c721bf-ab38-4264-a3e0-23388e62fcc1">
</p>



<br>


## Introduction
VisionCycle revolutionizes automated labeling for machine learning using Neural Radiance Fields (NeRF). Our algorithm, aptly named 'VisionCycle', starts by reconstructing 3D models from a minimal set of 2D images utilizing Instant NGP. It then renders these models from various angles to generate new 2D views. This cyclical transformation from 2D to 3D and back to 2D is central to our approach, enhancing the dataset generation process. Finally, VisionCycle automatically annotates these images with bounding boxes, readying them for YOLO training. This innovative cycle of vision makes the labeling process both efficient and scalable, pushing the boundaries of what automated systems can achieve in machine learning preparation.


<br>

<p align="center">
  <img src="[https://github.com/tersite1/tersite1/assets/160453556/41c721bf-ab38-4264-a3e0-23388e62fcc1](https://github.com/tersite1/tersite1/assets/160453556/bbe5a228-6dfe-43ab-a8c1-2bc1fe0390fe)">
</p>


<br>
<br>



## Pipeline Process
1. **2D to 3D Reconstruction**: Convert 2D photos to 3D models using Instant NGP.
2. **3D to 2D Rendering**: Render 3D models from various angles to produce new 2D images.
3. **Bounding Box Creation**: Auto-generate bounding boxes on the new 2D images.
4. **YOLO Training**: Use the images for machine learning model training.

<img width="1024" alt="스크린샷 2024-05-11 오후 10 32 06" src="https://github.com/tersite1/tersite1/assets/160453556/0b7cc713-7b17-4ba5-abbe-d7631e7e136d">


<img width="1100" alt="스크린샷 2024-05-12 오후 9 52 48" src="https://github.com/tersite1/tersite1/assets/160453556/28d91025-7970-435e-b29e-5aab94a5802c">


<br>
<br>




## Components Description
- **`NeRF.py`**: Executes Instant NGP to transform 2D images into 3D models.
- **`AutoCapture.py`**: Manages the rendering of 3D models into 2D views.
- **`AutoBounding.py`**: Automates bounding box creation in the new 2D images.






## Used Papers
- Gao, J., Shen, T., Wang, Z., Chen, W., Yin, K., Li, D., Litany, O., Gojcic, Z. and Fidler, S., 2022. Get3d: A generative model of high quality 3d textured shapes learned from images. Advances In Neural Information Processing Systems, 35, pp.31841-31854.
- Müller, T., Evans, A., Schied, C. and Keller, A., 2022. Instant neural graphics primitives with a multiresolution hash encoding. ACM Transactions on Graphics (TOG), 41(4), pp.1-15.


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




## Installation
```
git clone https://github.com/tersite1/VisionCycle.git
cd VisionCycle
pip install -r requirements.txt
```




## Usage

```
python3 main.py 'path_to_dataset'
```




## Contact
- Minsuk Jang - itcouldbe0@yonsei.ac.kr


## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgement

-  Support and funding from Yonsei University
-  Resources provided by NVIDIA





