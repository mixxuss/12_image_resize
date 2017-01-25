from __future__ import print_function
from PIL import Image
import os, argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to image')
    parser.add_argument('-w', '--width', help='Width of new image', default=None)
    parser.add_argument('-h', '--height', help='Height of new image', default=None)
    parser.add_argument('-s', '--scale', help='Scale to resize', default=None)
    parser.add_argument('-i', '--image', help='Image to resize path')
    parser.add_argument('-n', '--newimage', help='Path to new image')
    return parser


def open_image(path_to_original):
    image = Image.open(path_to_original)
    return image


def calculate_image_ratio(image_size):
    image_size_ratio = image_size[0]/image_size[1]
    return image_size_ratio


def calc_scale(image_size, new_width, new_height):
    if new_width:
        scale = new_width / image_size[0]
        return scale
    if new_height:
        scale = new_height / image_size[1]
        return scale


def resize_image(image, scale, path_to_result):
    new_size = (image.size[0] * scale, image.size[1] * scale)
    out_image = image.resize(new_size)
    out_image.save(path_to_result)


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    scale = args.scale
    new_width = args.width
    new_height = args.height
    image = open_image(args.image)
    if not scale:
        scale = calc_scale(image.size, new_width, new_height)
    resize_image(image, scale, args.newimage)

'''
    image = Image.open('123.jpg')
    print(image.format, image.size, image.mode)
    out_image = image.resize((250, 450))
    out_image.save('New.jpg')
'''