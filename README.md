# PixelPioneers: A Lightweight Python Library for Essential Image Processing

PixelPioneers is a lightweight Python library designed to perform basic image processing tasks, such as color representation and filtering. This library aims to provide a user-friendly interface and easy-to-understand functions for developers and researchers who require essential image processing capabilities without the extensive features of more complex libraries like OpenCV.

# Project Setup

    pip install -r requirements.txt
    pip install .

# Running the code

## CLI Help

```commandline
(venv) ameyk@Ameys-MBP finalprojects23-pixelpioneers % pixelpioneers -h
usage: pixelpioneers [-h] [-d | -v] -i IMAGES [IMAGES ...] -dest DEST {brightness,contrast,saturation,crop,flip,grayscale,invert,resize,rotate} ...

positional arguments:
  {brightness,contrast,saturation,crop,flip,grayscale,invert,resize,rotate}

options:
  -h, --help            show this help message and exit
  -d, --debug           Print lots of debugging statements
  -v, --verbose         Be verbose
  -i IMAGES [IMAGES ...], --images IMAGES [IMAGES ...]
                        List of source images
  -dest DEST            Destination directory
```

## Example 

```commandline
 pixelpioneers -d -i data/sample.bmp data/sample.jpeg -dest out resize 500 500
```