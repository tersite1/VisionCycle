

# VisionCycle: Auto Labeling Pipeline using NeRF


## Introduction
VisionCycle leverages Neural Radiance Fields (NeRF) to automate labeling processes for machine learning. It reconstructs a small number of 2D images into 3D using Instant NGP, renders the models from various angles to obtain new views, and automatically creates bounding boxes for YOLO training.

## Pipeline Process
1. **2D to 3D Reconstruction**: Convert 2D photos to 3D models using Instant NGP.
2. **3D to 2D Rendering**: Render 3D models from various angles to produce new 2D images.
3. **Bounding Box Creation**: Auto-generate bounding boxes on the new 2D images.
4. **YOLO Training**: Use the images for machine learning model training.

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

Install dependencies:

```bash
pip install -r requirements.txt
```

## Installation
```
git clone https://github.com/yourusername/VisionCycle.git
cd VisionCycle
pip install -r requirements.txt
```

## Usage

```
python3 main.py 'path_to_dataset'
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgement

-  Support and funding from Yonsei University
-  Resources provided by NVIDIA

## Contact
- Minsuk Jang - itcouldbe0@yonsei.ac.kr



