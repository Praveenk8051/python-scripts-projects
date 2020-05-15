import cv2
from tensorflow.python.platform import gfile
import ntpath
import os
import argparse


def create_file_list(path):
    file_list = []
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png']
    for extension in extensions:
        file_glob = os.path.join(path, '*.' + extension)
        file_list.extend(gfile.Glob(file_glob))

    return file_list


def resize_images(file_list, save_path):
    for i in range(len(file_list)):
        img = cv2.imread(file_list[i])
        resized_img = cv2.resize(img, (600, 600))
        head, tail = ntpath.split(file_list[i])
        new_path = save_path + '/' + tail
        print(new_path)
        cv2.imwrite(new_path, resized_img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--pick_files_path',
        type=str,
        default='',
        help='Path where files to be renamed reside'
    )
    parser.add_argument(
        '--save_files_path',
        type=str,
        default='',
        help='Path where files are to be saved'
    )
    args = parser.parse_args()
    file_list = create_file_list(args.pick_files_path)
    resize_images(file_list, args.save_files_path)
