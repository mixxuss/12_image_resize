from PIL import Image
import os
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', help='Width of new image', default=None, type=int)
    parser.add_argument('--height', help='Height of new image', default=None, type=int)
    parser.add_argument('--scale', help='Scale to resize', default=None, type=int)
    parser.add_argument('--image', help='Image to resize path')
    parser.add_argument('--newimage', help='Path to new image', default=None)
    return parser


def open_image(path_to_original):
    if os.path.exists(path_to_original):
        image = Image.open(path_to_original)
        return image
    else:
        raise FileNotFoundError('File not found, please check path to image')


def calculate_image_ratio(image_size):
    image_size_ratio = image_size[0]/image_size[1]
    return image_size_ratio


def calc_scale(image_size, new_width, new_height):
    if not new_width:
        scale = int(new_height) / image_size[1]
        return scale
    elif not new_height:
        scale = int(new_width) / image_size[0]
        return scale


def calculate_new_image_size(image, scale, new_width, new_height):
    if (not scale and not new_width) or (not scale and not new_height):
        scale = calc_scale(image.size, new_width, new_height)
        new_size = (int(image.size[0] * scale), int(image.size[1] * scale))
        return new_size
    elif new_width and new_height and not scale:
        new_size = (int(new_width), int(new_height))
        if calculate_image_ratio(new_size) != calculate_image_ratio(image.size):
            print('Will be a crooked image')
        return new_size
    elif scale:
        new_size = (int(image.size[0] * scale), int(image.size[1] * scale))
        return new_size
    else:
        raise SyntaxError('Too many arguments given.')


def calculate_new_image_path(path_to_original, path_to_new, new_size):
    original_filepath, original_extension = os.path.splitext(path_to_original)
    if path_to_new is None:
        new_image_name_and_path = str(original_filepath) + '__' + str(new_size[0]) + 'x' \
                                  + str(new_size[1]) + str(original_extension)
        return new_image_name_and_path
    new_image_name_and_path = path_to_new
    return new_image_name_and_path


def resize_image(image, new_size, new_image_name_and_path):
    out_image = image.resize(new_size)
    out_image.save(new_image_name_and_path)
    print('Saved to', new_image_name_and_path)


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    path_to_original = args.image
    scale = args.scale
    new_width = args.width
    new_height = args.height
    path_to_new = args.newimage
    image = open_image(args.image)
    new_size = calculate_new_image_size(image, scale, new_width, new_height)
    new_image_name_and_path = calculate_new_image_path(path_to_original, path_to_new, new_size)
    resize_image(image, new_size, new_image_name_and_path)
