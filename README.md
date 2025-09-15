# Computer Vision Toolkit

Simple OpenCV tools for image conversion, channel operations, shifting, noise, blurring, and difference images.

## Overview
The scripts read two input images and generate a set of outputs for each image. Outputs include grayscale, HSV, per channel images, a red to green swap, a shifted image, salt and pepper noise, a blurred version, and a difference image.

## Files in this repo
- `wrapper.py` runs the full pipeline on two images  
- `hw1.py` contains the image functions  
- `hw1_pic1.jpg` and `hw1_pic2.jpg` are sample inputs  
- Generated outputs are saved in the repo folder:
  - `hw1_pic1_gray.jpg`, `hw1_pic2_gray.jpg`
  - `hw1_pic1_hsv.jpg`, `hw1_pic2_hsv.jpg`
  - `hw1_pic1_red.jpg`, `hw1_pic1_green.jpg`, `hw1_pic1_blue.jpg` and the same for pic2
  - `hw1_pic1_swapped.jpg`, `hw1_pic2_swapped.jpg`  (red and green swapped)
  - `hw1_pic1_shifted.jpg`, `hw1_pic2_shifted.jpg`
  - `hw1_pic1_sp.jpg`, `hw1_pic2_sp.jpg`  (salt and pepper noise)
  - `hw1_pic1_sp_blur.jpg`, `hw1_pic2_sp_blur.jpg`  (blur applied after noise)
  - `hw1_pic1_difference.jpg`, `hw1_pic2_difference.jpg`
  - Optional per channel noise files:
    `hw1_pic*_noise_red.jpg`, `hw1_pic*_noise_green.jpg`, `hw1_pic*_noise_blue.jpg`
    
## Environment
    pip install opencv-python numpy

## How to run
    # default run on the two sample images
    python wrapper.py

To use different images, edit the file paths at the top of `wrapper.py`.

## What each stage does
- Convert to grayscale and HSV  
- Extract red, green, and blue channels  
- Swap red and green channels  
- Shift the image by a fixed pixel offset  
- Add salt and pepper noise, then blur to reduce it  
- Compute an absolute difference image
