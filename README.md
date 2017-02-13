# Image Resizer

This program changing size of image specify set by the user

# Installing requirements

Packages installing by command
```
pip install -r requirements.txt
```

# Example
```
usage: image_resize.py [-h] [--width WIDTH] [--height HEIGHT] [--scale SCALE]
                       [--image IMAGE] [--newimage NEWIMAGE]

optional arguments:
  -h, --help           show this help message and exit
  --width WIDTH        Width of new image
  --height HEIGHT      Height of new image
  --scale SCALE        Scale to resize
  --image IMAGE        Image to resize path
  --newimage NEWIMAGE  Path to new image
```

# Example

```
python3 image_resize.py --image /12_image_resize/123.png --scale 3
Saved to /12_image_resize/123__3069x1518.png
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
